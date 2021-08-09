try:
    name=input("Enter your name: ")
    if name=='john':
        raise ValueError("John is not allowed!")
    else:
        print("Hello ",name)
except Exception as e:
    print(e.args)

