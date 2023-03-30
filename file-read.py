#Print all the lines at once
f=open("sample2.txt","r")
contents = f.read()
print(contents)
f.close()

#print line by line
f=open("sample2.txt","r")
print(f.readline())
print(f.readline())
f.close()

#Read all lines into a list
f=open("sample2.txt","r")
lines = f.readlines()
print(lines)
f.close()

# print 1st line
print(lines[0])

# print 4th line
print(lines[3])
