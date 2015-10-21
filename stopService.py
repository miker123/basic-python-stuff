#!/usr/bin/env python
#Mike R
#Queries User for service to kill. Then kills script. Written using Python 3.5

import os
service=input("Which service to kill: ")

#Kills the service by running the command in the command prompt. Works with Windows only
os.system('sc stop ' + service)
