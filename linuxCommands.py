#!/usr/bin/env python

import os

#Capture the disk free space
os.system("df -h > diskSpace.txt")

#display the free memory usage
os.system("free > memoryUsage.txt")

#all TCP sockets
os.system("ss -t -a > allTCPSock.txt")

#all UDP Sockets
os.system("ss -u -a > allUDPSock.txt")

#display all sockets
os.system("ss -a > allSockets.txt")

#display all processes
os.system("ps -aux > processes.txt")

#Display all available commands
os.system("compgen -c > allCMDs.txt")

#List linux namespaces
os.system("lsns" > namespaces.txt)
