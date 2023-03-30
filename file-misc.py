# how to open a file using absolute path windows style

f=open("c:\\users\\admin\\desktop\\data.txt","r")
print(f.read())
f.close()

# how to open a file using absolute path linux style
f=open("c:/users/admin/desktop/data.txt","r")
print(f.read())
f.close()

# print the number of characters in a file
f=open("c:/users/admin/desktop/data.txt","r")
print(len(f.read()))
f.close()

# print the number of lines in a file
f=open("c:/users/admin/desktop/data.txt","r")
print(len(f.readlines()))
f.close()

# working with the "with" statement

with open("c:/users/admin/desktop/data.txt","r") as f:
    print(f.closed)
    print(f.read())
print(f.closed)
