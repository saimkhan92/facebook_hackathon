import sys
import commands
container_name=sys.argv[1]
#argument2=sys.argv[2]
#print ("This is the first argument:",argument1)
#print ("This is the second argument:",argument2)
command="docker run -itd --name="+str(container_name)+" "+"busybox"
container_id=str(commands.getoutput(command))
print("Congratulations! A new docker container has been created!")
#if True==True:
#	network_names=commands.getoutput('docker network ls|tr -s " "|cut -d " " -f2|sed 1d')
#	out = ''
#	for i in network_names.split('\n'):
#		out = out +i+ ','
#	print out
