import sys
import commands
#argument1=sys.argv[1]
#argument2=sys.argv[2]
#print ("This is the first argument:",argument1)
#print ("This is the second argument:",argument2)
if True==True:
	container_names=commands.getoutput('docker ps|tr " \+" "@"|sed 1d')
	out = ''

	for i in container_names.split('\n'):
		out = out + i[i.rfind('@')+1:] + ','

	print out
