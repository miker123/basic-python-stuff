#!/usr/bin/env python
#Author: Mike R
import os, time

#gets file stats on specific file
def fileStats(file):
	mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = file
	print "Owner is ",str(uid)
	print "Size is " + str(size) + " bytes"
	print "Last modified at %s" %time.ctime(mtime)
	print "Group ID of owner is ", str(gid)
	print "File is ", str(size) , " bytes in size"

fileInfo=input('What file to examine: ')
stats = os.stat(fileInfo)
fileStats(stats)
