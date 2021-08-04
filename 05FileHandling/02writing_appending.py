# file=open('./test.txt','w')
# file.write("AFTER\n")
# file.write("Hwllooo")
# file.writelines(["Hey\n","How are you\n"])
# file.close()


file=open('./test.txt','a')
file.write("AFTER\n")
file.write("Hwllooo")
file.writelines(["Hey\n","How are you\n"])
file.close()