#!/usr/bin/env python
#Get the uname information
import subprocess
from subprocess import check_output

#Actual Program
releaseNo=check_output('uname -r', shell=True, executable='/bin/bash')
hostname=check_output('uname -n', shell=True, executable='/bin/bash')
kernalName=check_output('uname -s', shell=True, executable='/bin/bash')
processor=check_output('uname -p', shell=True, executable='/bin/bash')
#hardware=check_output('uname -i', shell=True, executable='/bin/bash')
outputAll=check_output('uname -a', shell=True, executable='/bin/bash')

#writes all of the commands line by line to the file. 
f=open('linxCommands.txt', 'w')
f.write("List of the uname information:")
f.write("\n")
f.write("Release info: " + releaseNo)
f.write("\n")
f.write("hostname: " + hostname)
f.write("\n")
f.write("Kernal Name: " + kernalName)
f.write("\n")
f.write("Processor Information: " + processor)
f.write("\n")
#f.write("Hardware Information: " + hardware)
#f.write("\n")
f.write("All Info: " + outputAll)
f.write("\n")
