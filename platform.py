#/usr/bin/env python
#Author: Mike R
#get information about host. A mishmash of stuff.


import platform
import OS

#Returns the computer’s network name (may not be fully qualified!). An empty string is returned if the value cannot be determined.
print platform.node()

#Fairly portable uname interface. Returns a tuple of strings (system, node, release, version, machine, processor) identifying the underlying platform. Entries which cannot be determined are set to ''.
print platform.node()

#Get additional version information from the Windows Registry and return a tuple (release, version, csd, ptype) referring to OS release, version number, CSD level (service pack) and OS type (multi/single processor).
platform.win32_ver()

#Get Mac OS version information and return it as tuple (release, versioninfo, machine) with versioninfo being a tuple (version, dev_stage, non_release_version). Entries which cannot be determined are set to ''. All tuple entries are strings.
platform.mac_ver()

#Tries to determine the name of the Linux OS distribution name.
platform.linux_distribution()

#get all connections. Provide all data. And then 
os.system("netstat")
