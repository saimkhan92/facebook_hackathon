import sys
import commands
container_name=str(sys.argv[1])
network_name=str(sys.argv[2])
#argument2=sys.argv[2]
#print ("This is the first argument:",argument1)
#print ("This is the second argument:",argument2)
command="docker network connect "+str(network_name)+" "+str(container_name)
output=commands.getoutput(command)
print("Congratulations!"+container_name+" has been connected to " +network_name)





#if True==True:
#	network_names=commands.getoutput('docker network ls|tr -s " "|cut -d " " -f2|sed 1d')
#	out = ''
#	for i in network_names.split('\n'):
#		out = out +i+ ','
#	print out
