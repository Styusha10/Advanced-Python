f = open("text.txt", "w")

def write_array(f, arr):
    f.writelines(arr)
    pass
arr = ["hello", "world", "hello", "sun"]
arr = map(lambda x: x + '\n', arr)
write_array(f, arr)
f.close()

f = open("text.txt", "r")
for line in f: print(line.strip())
f.close()
