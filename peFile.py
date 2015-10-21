#!/usr/bin/python
#Author: Mike R
import pefile
import pprint

#---------------------------------------------------------------
#show DOS header

def dosHeader(pe): 
	print pe.DOS_HEADER
	print "\n"


#---------------------------------------------------------------
#show file Header
def fileHeader(pe):
	print pe.FILE_HEADER
	print "\n"

#---------------------------------------------------------------
#show NT Header
def ntHeader(pe):
	print pe.NT_HEADERS
	print "\n"

#---------------------------------------------------------------
#show Optional Header
def optionalHeader(pe):
	print pe.OPTIONAL_HEADER
	print pe.OPTIONAL_HEADER.SectionAlignment
	print pe.OPTIONAL_HEADER.FileAlignment
	print pe.OPTIONAL_HEADER.CheckSum
	print "\n"

#---------------------------------------------------------------
#check for imports
#pair with this site to find what it is: http://dll.paretologic.com/detail.php/SHLWAPI 

def imports(pe):
	try:
		print "Checking Imports"
		for entry in pe.DIRECTORY_ENTRY_IMPORT:
			print "\t" + entry.dll
			for imp in entry.imports:
				print "\t\t" + str(imp.name)

	except AttributeError:
		print "The file has no imports\n"

#---------------------------------------------------------------
#check for exports
def exports(pe):
	try:

		print "\nChecking Exports"
		for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        		print hex(dll.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal

	except AttributeError:
		print "The file has no exports\n"

#---------------------------------------------------------------
#show resources
def showResources(pe):
	strings = list()

	rt_string_idx = [entry.id for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_STRING'])
	rt_string_directory = pe.DIRECTORY_ENTRY_RESOURCE.entries[rt_string_idx]

	for entry in rt_string_directory.directory.entries:
  		data_rva = entry.directory.entries[0].data.struct.OffsetToData
 		size = entry.directory.entries[0].data.struct.Size
  		print 'Directory entry at RVA', hex(data_rva), 'of size', hex(size)

 
 		data = pe.get_memory_mapped_image()[data_rva:data_rva+size]
  		offset = 0
  		while True:
    			if offset>=size:
    				break
   
   			ustr_length =pe.get_word_from_data(data[offset:offset+2], 0)
    			offset += 2
    			if ustr_length==0:
      				continue
    			ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=ustr_length)
    			offset += ustr_length*2
    			strings.append(ustr)
    			print 'String of length', ustr_length, 'at offset', offset

#---------------------------------------------------------------
#Show debug
#IMAGE_DIRECTORY_ENTRY_DEBUG
def debugIt(pe):
	for dbg in pe.DIRECTORY_ENTRY_DEBUG:
                
		print dbg


#---------------------------------------------------------------
# 			Main Program
#---------------------------------------------------------------
#ask user for file

#Make sure to get full path before loading PE
fileInput=raw_input("What file will be examined?")
fileInput=str(fileInput)

#loading a file
pe=pefile.PE('C:\\Program Files (x86)\\Kontiki\\KService.exe')

#---------------------------------------------------------------
#Print out sections available to choose from so user can pick what to print
while(True):
	try:
		outputSelection=raw_input("Options to Examine:\n1)DOS Header\n2)File Header\n3)NT Header\n4)Optional Header\n5)Imports\n8)Exports\n7)Resources\n8)Debug\n9)Quit\nWhat should be examined?")

		outputSelection=int(outputSelection)

		if outputSelection==1:
			dosHeader(pe)
		elif outputSelection==2:
			fileHeader(pe)
		elif outputSelection==3:
			ntHeader(pe)
		elif outputSelection==4:
			optionalHeader(pe)
		elif outputSelection==5:
			imports(pe)
		elif outputSelection==6:
			exports(pe)
		elif outputSelection==7:
			showResources(pe)
		elif outputSelection==8:
			debugIt(pe)
		elif outputSelection==9:
			break


	except:
		print "Please select a number in the future"


