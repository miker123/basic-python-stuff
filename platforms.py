#!/usr/bin/env python
#Author: Mike R
#Goal of program is to obtain platform information as well as information about:
#Platform Services
#Platform Programs and Directories
#Ports Open and Internet Address

#Next step is to write information from output to files

#Author: Michael Radov
#Date: 5/1/2015

import platform
import os
import subprocess

#-----------------------------------------------------
#walk the directories and files on a linux machine
def walkLinux():
	lFiles=open("linuxFiles.txt", "w")
	print "Walking Linux directories and files-->Writing data to linuxFiles.txt"
	for root, direct, files in os.walk('/'):
		path=root.split("/")
		paths=((len(path)-1)*'-',os.path.basename(root))
		lFiles.write(str(paths))
		for file in files:
			data=len(path)*'-', file
			lFiles.write(str(data))
	lFiles.close()
#-----------------------------------------------------
def unixServices():
	lService=open("linuxServices.txt", "w")
	print "Enumerating Linux Services and writing files to linuxServices.txt\n"
	output=subprocess.check_output(['ps', '-A'])
	lService.write(output + "\n")
	lService.close()
#-----------------------------------------------------
#Walk Windows FileSystem
def walkWindows():
	wFiles=open("windowsFiles.txt", "w")
	print "Walk through Windows Directory and writing to windowsFiles.txt"
	for path,dirs,files in os.walk('c:\\'):
		wFiles.write(path)
		for f in files:
			wFiles.write(f)
	wFiles.close()
#-----------------------------------------------------
#Get Windows Services
def windowsServices():
	wService=open("windowsServices.txt", "w")
	print "Windows Services"
	output=subprocess.check_output(['sc', 'query'])
	wService.write(output)
	wService.close()
#-----------------------------------------------------
	

#Main Program
#get platform of the machine and run some commands. Can be more exact with type of system
if "Windows" in platform.platform():
	print "It's a Windows system"
	walkWindows()
	windowsServices()

elif "Darwin" in platform.platform():
	print "It's an OS X system"
	walkLinux()
	unixServices()
	
elif "Linux" in platform.platform():
	print "It's a Linux system"
	walkLinux()
	unixServices()
