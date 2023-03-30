import os
import time

print(os.listdir())

for myfile in os.listdir():
    print(myfile, os.path.getsize(myfile), time.ctime(os.path.getctime(myfile)))
