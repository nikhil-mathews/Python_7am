'''
it is a way of writing programs
it is based DRY principle (Do not repeat yourself)
It is a set of code which we can use as per our usage

'''

# def function_name():
#     //statements

# def greet():
#     print("Hello There!!")
    # return


# Calling the function
# greet()
# print("Further code!")
# greet()


# def sayHello(name):
#     print(f"Hello, {name}")

# sayHello("Nikhil")
# sayHello("Javeed")

# def sayHello(name,age):
#     print(f"Hello,{name}")

# sayHello(age=15,name="John")

# Default arguments
# def profile(name='NA',age='NA'):
#     print(f"{name} and {age}")

# profile("John",14)
# profile()

# returning value
# def calc(num1,num2):
#     add=num1+num2
#     sub=num1-num2
#     return (add,sub)

# (ans1,ans2)=calc(3,5)
# print(ans1)
# print(ans2)

# print(calc(6,8))


# Variable length arguments
# def func(*a):
#     print(type(a))
#     count=0
#     sum=0
#     for i in a:
#         sum=sum+i
#         count=count+1
#     else:
#         print(f"sum is {sum} and count is {count}")

# func(1,2,3,4,5,6,7)
# func()


# variable length keyword arguments
# def func(age,**kwargs):
#     print(age)
#     for k,v in kwargs.items():
#         print(f"{k}--->{v}")
    

# func(age=45,Fname="John",lname="Doe")

# lambda functions(anonymous function)

# def cube(x):
#     return x*x*x

# cube=lambda x : x*x*x
# print(cube(3))

add=lambda a,b:a+b

# print(add(2,4))

# map-> creating a new sequence from existing one
nums=[1,4,6,7,3,2]

# sqr=list(map(lambda x:x*x,nums))
# print(sqr)



# filter--> to filter the sequence
# even=list(filter(lambda x: x%2==0,nums))
# odd=list(filter(lambda x: x%2!=0,nums))
# print(even)
# print(odd)

# reduce
# from functools import reduce

# sum=reduce(lambda a,b:a+b,nums)
# print(sum)


