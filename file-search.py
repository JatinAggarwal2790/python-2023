# search a file for a word

filename = "sample2.txt"
pattern = "Two"

with open(filename,'r') as f:
    for lineno, line in enumerate(f):
        if pattern in line:
            print(lineno + 1, line.rstrip())


with open(filename,'r') as f:
    for lineno, line in enumerate(f,1):
        if pattern.lower() in line.lower():  # case insensitive search
            print(lineno, line, end="")
