#!/usr/bin/env python
#Author: Mike R
#Search specific file and see if the desired output is there.
#If specific output is there, then print the line

dmesg = open("/var/log/messages", "r")
for line in dmesg.readlines():
        if ("usb" or "USB") in line:
                print line
dmesg.close()
