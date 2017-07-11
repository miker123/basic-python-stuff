#!/usr/bin/env python

import subprocess
from subprocess import check_output


output=check_output('echo $PATH', shell=True, executable='/bin/bash')
f=open('linxCommands.txt', 'w')
f.write("$Path in which the shell seaches through when entering a command:")
f.write("\n")
f.write(output)
f.write("\n")

#get environment variables
envOutput=check_output('env', shell=True, executable='/bin/bash')
f.write("Environment Variables:")
f.write("\n")
f.write(envOutput)
f.write("\n")
