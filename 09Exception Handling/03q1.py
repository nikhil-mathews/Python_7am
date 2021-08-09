def func():
    try:
        return 1
    except: 
        return 2
    finally:
        return 3

print(func())

