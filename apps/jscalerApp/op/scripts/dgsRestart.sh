killall DiagGuiServer

# mutexclean, per Sergey's recommendation, added December 16, 2017
# Totally untested.  I added a sleep just to be safe.  (NAB)
mutexclean ; sleep 2

exec DiagGuiServer >& /dev/null &

