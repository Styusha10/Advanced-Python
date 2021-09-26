import zipfile
import os

arr = []

f = open("text3.txt", "w")
for current_dir, dirs, files in os.walk("main"):
    for fl in files:
        if fl.endswith('.py'):
            arr.append(current_dir)
            break

arr.sort()
arr = map(lambda x: x + '\n', arr)
f.writelines(arr)
f.close()

f = open("text3.txt", "r")
for line in f: print(line.strip())
f.close()
