# a=7

def outer():
    a=5
    print("Outer: ",a)

    def inner():
        # a=9
        nonlocal a
        a=19
        print("Inner: ",a)
    inner()

    print("After: ",a)


outer()
# print("Main: ",a)