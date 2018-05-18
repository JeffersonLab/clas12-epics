# Cyber

The lists in ./lists/ determine cyber scanning for HallB.  They are provided 
to the Cyber Team via URL.  This configured in the the docker-run.sh.  

docker-run.sh - start/restart the webserver
host_lookup.py - read host lists and report back associated hostname

lists/hallb_d.txt - hosts exluded from discovery scans
lists/hallb_v.txt - hosts exluded from vulnerability scans

