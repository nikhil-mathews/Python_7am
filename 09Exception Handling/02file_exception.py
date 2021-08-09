try:
    file=open('test.txt','r')
except FileNotFoundError as e:
    print(e)