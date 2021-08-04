'''
rb
wb
ab
'''

file=open('./t1.png','rb')
file2=open("./copy.png",'wb')
# data=file.read()
for i in file:
    file2.write(i)
file.close()
file2.close()