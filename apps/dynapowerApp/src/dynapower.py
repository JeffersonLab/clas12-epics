#!/usr/bin/env python3
import re,sys,socket,logging,argparse,datetime,epics

# There appears to be a bug in the EPICS asyn module, even the latest 4-42, where
# I/O Intr records can cause deadlock.  Here we workaround that by manually parsing
# the periodic, unsolicited messages from the Dynapower and just write to soft PVs.

sys.path.insert(0,' /usr/clas12/third-party-libs/pyepics3.5.0-RHEL7/lib/python3.6/site-packages')

class DynapowerPV():

  def __init__(self, name, message_group, is_hex):
    self.pv = epics.PV(name)
    self.group = message_group
    self.is_hex = is_hex

class DynapowerMessage():

    terminator = r'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    regex = b'^ \r\n (\d+) \r\n (\d+) \r\n (\d+) \r\n (\d+) \r\n (\d\d\d\d) \r\n (\d\d\d\d) \r\n (\d\d\d\d)\r'
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
            logging.getLogger(__name__).warning('Invalid format:  '+str(byte_string))
        else:
            logging.getLogger(__name__).debug('Debug data:  '+str(byte_string))
        return m

    def _update(self, match):
        self.previous_timestamp = self.timestamp
        self.timestamp = datetime.datetime.now()
        self.raw_data = match.group(0)
        for k,v in DynapowerMessage.pvs.items():
            if v.is_hex is True:
                self.data[k] = int(match.group(v.group),16)
            else:
                self.data[k] = float(match.group(v.group))/10

    def _publish(self, match=None):
        if match is not None:
            self._update(match)
        for k,v in DynapowerMessage.pvs.items():
            v.pv.put(self.data[k])

    def parse_and_publish(self, byte_string):
        m = DynapowerMessage.parse(byte_string)
        if m is None:
            return False
        else:
            self._publish(m)
            return True

if __name__ == '__main__':

    cli = argparse.ArgumentParser(description='asdf')
    cli.add_argument('-debug', help='enable debugging verbosity', default=False, action='store_true')
    cli.add_argument('host', help='host name', type=str)
    cli.add_argument('port', help='port number', type=int)
    args = cli.parse_args(sys.argv[1:])

    if args.debug: logging_level = logging.DEBUG
    else:          logging_level = logging.INFO
    logging.basicConfig(level=logging_level, format='%(message)s')

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

                if dyna.timestamp is not None:
                    msg = 'Update: ' + str(dyna.timestamp)
                    if dyna.previous_timestamp is not None:
                        msg += ' ==> Period: ' + str(dyna.timestamp-dyna.previous_timestamp)
                    logging.getLogger(__name__).info(msg)

            data = b''

