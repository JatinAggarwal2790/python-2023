#Write a program that will search for a word in a file.
#The program must print the line number of the matched
#line and also its contents

import sys

filename = sys.argv[1]
pattern = sys.argv[2]

f=open(filename,'r')
for lineno,line in enumerate(f):
    if pattern.lower() in line.lower():
        print(lineno +1, line, end="")
f.close()
