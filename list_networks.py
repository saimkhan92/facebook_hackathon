import sys
import commands
#argument1=sys.argv[1]
#argument2=sys.argv[2]
#print ("This is the first argument:",argument1)
#print ("This is the second argument:",argument2)
if True==True:
	network_names=commands.getoutput('docker network ls|tr -s " "|cut -d " " -f2|sed 1d')
	out = ''
	for i in network_names.split('\n'):
		out = out +i+ ','
	print out
