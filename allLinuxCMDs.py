#!/usr/bin/env python

#Author: Mike R
#Date: 10/1/2015
#Purpose: Program to find OS Info

#imports
import subprocess
from subprocess import check_output


#Actual Program
output=check_output('compgen -c', shell=True, executable='/bin/bash')
commands=output.splitlines()

#print list of all commands
#print commands


#writes all of the commands line by line to the file. 
f=open('linxCommands.txt', 'w')
for word in commands:
	f.write(word)
	f.write("\n")


