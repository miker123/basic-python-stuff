#print all arguments to the program after python program.py arg arg2 
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
print count
i=count + 1
c = 1
while c < i:
    print sys.argv[c]
    c+=1
