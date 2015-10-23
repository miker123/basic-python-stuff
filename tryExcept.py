#/usr/bin/env python

#Author: Mike R
#Date:10/23/2015
#Purpose:Show an example try/except statement

#use Input instead of raw_input in Python 3.5 and above
test=raw_input("Please input a number: ")

#Testing to see if the user used a number or not
try:
	test=int(test)
except:
	print "Please insert a whole number"
