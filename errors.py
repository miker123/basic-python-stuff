#!/usr/bin/env python
import os
#Author: Mike R
#This program will write and then run a VBS script that will pop up errors to the user. 
#For more information about writing error files, http://www.wikihow.com/Make-a-Fake-Error-Message-on-Windows

with open("test.vbs", "a") as myfile:
	myfile.write("x=msgbox(\"Message Here\",0+0,\"Title Here\")\n")
	myfile.write("x=msgbox(\"Message Here\",0+0,\"Title Here\")\n")
	myfile.write("x=msgbox(\"Message Here\",0+0,\"Title Here\")\n")

#Run the file!	
os.startfile("test.vbs")
