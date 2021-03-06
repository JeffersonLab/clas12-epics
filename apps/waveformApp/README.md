# waveformApp

Just a sequencer to read a list of PV names from a file and
periodically update their values in an output waveform.

### Example ioc startup commands:
```
dbLoadRecords("db/waveformApp.db","P=a:,R=1:,NELM=100,FTVL=FLOAT,PERIOD=5,FNAME=pvList1.txt")
dbLoadRecords("db/waveformApp.db","P=a:,R=2:,NELM=800,FTVL=FLOAT,PERIOD=5,FNAME=pvList2.txt")
seq waveform, "P=a:,R=1:"
seq waveform, "P=a:,R=2:"
```
Where output waveforms would be in `a:1:wf` and `a:2:wf`,
and NELM should be at least as large as number of PVs in FNAME.

### Performance Test:
In one IOC:
* 52 simultaneous sequencers (each with one output waveform)
  * most with ~200 long waveforms
  * two with 5K long waveforms
  * one with a 20K long waveform
  * with waveform update period of 5 seconds
* 40K total input PVs
* Resource Usage
  * Memory 1.4 GB
  * Peak CPU usage of 4.6% (Intel Xeon E5-2620 2.4 GHz)
    * decreasing update period by 5X (to 1 second) increased CPU usage by 3X
    * sleep instead of delay gives 2X CPU reduction, although may miss pvMonitor updates(?)

### TODO:
- [ ] confirm it works on vxWorks

