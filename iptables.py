#!/usr/bin/env python
import fileinput 

import os
import sys
import subprocess



service=sys.argv[1]

chain=sys.argv[2]

#service="HTTP"
#perm=arg2
#chain="INPUT"


f= open('/root/capirca/policies/pol/sample_speedway.pol','rw')
lines=f.readlines()
f.close()
if(chain=="INPUT"):
	#print lines
	#f.close()
	i=lines.index("  target:: speedway INPUT DROP\n")
	print i
	if(i > 0):	
 		print"Inside if"
		i=i+2
		term="""term base-allow-"""+service+"""-in { 
		protocol:: tcp
		destination-port::""" +service+"""\n\
		action:: accept
		}\n"""
	
 		lines.insert(i,term )
		print lines
		str=''
		str=''.join(lines)
	
		print(str)
		with open('/root/capirca/policies/pol/sample_speedway.pol','w') as file:
	
			file.writelines(str)
			file.close()


if(chain=="OUTPUT"):
	#print lines1
	#f.close()
	i=lines.index("  target:: speedway OUTPUT DROP\n")
	print i
	if(i > 0):	
 		print"Inside if"
		i=i+2
		term="""term base-allow-"""+service+"""-in { 
		protocol:: tcp
		destination-port::""" +service+"""\n\
		action:: accept
		}\n"""
	
 		lines.insert(i,term )
		print lines
		str=''
		str=''.join(lines)
	
		print(str)
	
if(chain=="FORWARD"):
	#print lines
	#f.close()
	i=lines.index("  target:: speedway FORWARD DROP\n")
	print i
	if(i > 0):	
 		print"Inside if"
		i=i+2
		term="""term base-allow-"""+service+"""-in { 
		protocol:: tcp
		destination-port::""" +service+"""\n\
		action:: accept
		}\n"""
	
 		lines.insert(i,term )
		print lines
		str=''
		str=''.join(lines)
	
		print(str)



subprocess.call(' python ~/capirca/aclgen.py',shell='TRUE')

