#!/usr/bin/env python
import os
#Author: Michael Radov
#Python program that works on Windows to query for services and writes data to file. 

os.system('sc query > services.txt')
#file gets written to working directory
