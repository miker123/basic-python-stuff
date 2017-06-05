#!/usr/bin/env python
#This will parse the arguments that are not the file name
import sys
argLen= len(sys.argv)

for var in sys.argv:
  if var is not sys.argv[0]:
    print var
