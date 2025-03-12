#!/usr/bin/env python3
import re,sys,socket,logging,argparse,datetime,epics

#
# N. Baltzell, 2022
#
# There appears to be a bug in the EPICS asyn module, even the latest 4-42, where
# I/O Intr records can cause deadlock.  Here we workaround that by manually parsing
# the periodic, unsolicited messages from the Dynapower and just write to soft PVs.
# This requires an additional heartbeat PV for alarming on loss of comms.

sys.path.insert(0,' /usr/clas12/third-party-libs/pyepics3.5.0-RHEL7/lib/python3.6/site-packages')

class DynapowerPV():

  def __init__(self, name, message_group, is_hex):
    self.pv = epics.PV(name)
    self.group = message_group
    self.is_hex = is_hex

class DynapowerMessage():

    terminator = r'\x00' * 12

    regex = b'^\r\n (\d+)\r\n (\d+)\r\n (\d+)\r\n (\d+)\r\n (\d+)\r\n (\d+)\r\n (\d+)'

    re.compile(regex)

    pvs = {}
    pvs['volt'] = DynapowerPV('DYNAB:v:rbk',    1, False )
    pvs['amps'] = DynapowerPV('DYNAB:i:rbk',    2, False )
    pvs['temp'] = DynapowerPV('DYNAB:temp',     3, False )
    pvs['flow'] = DynapowerPV('DYNAB:flow',     4, False )
    pvs['stat'] = DynapowerPV('DYNAB:stat:rbk', 5, True )
    pvs['flt1'] = DynapowerPV('DYNAB:fault:1',  6, True )
    pvs['flt2'] = DynapowerPV('DYNAB:fault:2',  7, True )

    def __init__(self):
        self.data = {}
        self.raw_data = None
        self.timestamp = None
        self.previous_timestamp = None

    @staticmethod
    def is_terminated(byte_string):
        return str(byte_string).find(DynapowerMessage.terminator) >= 0

    @staticmethod
    def parse(byte_string):
        m = re.match(DynapowerMessage.regex, byte_string)
        if m is None:
            logging.getLogger(__name__).warning('Invalid  format:  '+str(byte_string))
        else:
            logging.getLogger(__name__).info('Expected format:  '+str(byte_string))
        return m

    def _update(self, match):
        self.previous_timestamp = self.timestamp
        self.timestamp = datetime.datetime.now()
        self.raw_data = match.group(0)
        for k,v in DynapowerMessage.pvs.items():
            try:
                if v.is_hex is True:
                    self.data[k] = int(match.group(v.group),16)
                else:
                    self.data[k] = float(match.group(v.group))/10
            except Exception as e:
                print(e)

    def _publish(self):
        for k,v in DynapowerMessage.pvs.items():
            try:
                v.pv.put(self.data[k])
            except Exception as e:
                print(e)

    def parse_and_publish(self, byte_string):
        m = DynapowerMessage.parse(byte_string)
        if m is not None:
          self._update(m)
          self._publish()
        return m is not None

if __name__ == '__main__':

    cli = argparse.ArgumentParser(description='asdf')
    cli.add_argument('-logging', help='logging level', type=str, default='WARNING', choices=['DEBUG','INFO','WARNING','CRITICAL'])
    cli.add_argument('-host', help='host name', type=str, default='hallb-moxa6')
    cli.add_argument('-port', help='port number', type=int, default=4009)
    args = cli.parse_args(sys.argv[1:])

    if args.logging == 'CRITICAL':
      level = logging.CRITICAL
    elif args.logging == 'WARNING':
      level = logging.WARNING
    elif args.logging == 'INFO':
      level = logging.INFO
    elif args.logging == 'DEBUG':
      level = logging.DEBUG

    logging.basicConfig(level=level, format='%(message)s')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.host,args.port))
    logging.getLogger(__name__).info('Connected to %s:%d'%(args.host,args.port))

    data = b''
    dyna = DynapowerMessage()

    while True:

        data += sock.recv(1)
        logging.getLogger(__name__).debug('DATA: >%s<'%(str(data)))

        if dyna.is_terminated(data):

            if dyna.parse_and_publish(data):

                msg = 'Update: ' + str(dyna.timestamp)
                if dyna.previous_timestamp is not None:
                    msg += ' ==> Period: ' + str(dyna.timestamp-dyna.previous_timestamp)
                logging.getLogger(__name__).info(msg)

            data = b''

