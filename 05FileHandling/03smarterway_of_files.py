from os import W_OK


with open('./test.txt','r') as f:
    data=f.readlines()
    for line in data:
        word=line.split()
        print(word)

print("file will get closed automatically")