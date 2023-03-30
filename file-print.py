f=open("sample2.txt","r")
for line in f:
    print(line, end="")
f.close()

print("\n-----------")
f=open("sample2.txt","r")
for line in f:
    print(line.rstrip())
f.close()
