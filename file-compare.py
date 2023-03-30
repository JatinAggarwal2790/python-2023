import filecmp

file1 = "sample.txt"
file2 = "sample2.txt"

print(filecmp.cmp(file1, file2))
