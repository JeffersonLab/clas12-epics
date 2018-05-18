
rollAvgApp

Report time-averages of EPICS PVs based on Mya archiving
* rolling averages periodically updated for previous N-hours
* 2-hour, 8-hour, 24-hour, and 1-week

Built with 
* a softioc just to host PVs
** N-hour averages and their alarm limits
** status of communications with Mya archive
* a multithreaded python script
** preiodically polls the Mya archive with myStats command line tool
** with polling periods proportional to time span of the averaging
** one thread per polling period

Would be better to replace python script with an EPICS driver for retrieving time-averages from Mya using the Mya C++ API.


