'''
text
binary
r-reading
w-writing
a-appending
r+ for both reading and writing
'''

file=open('../01basics/00hello.py','r')

# print(file)
# data=file.read(5)
# print(data)

# for con in file:
#     print(con,end='')

# data=file.readlines()[0]

# print(data)

# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.seek(5)
# print(file.read())

# print("File opened successfully")
file.close()