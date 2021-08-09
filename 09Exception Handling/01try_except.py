num1=5
num2=6

try:

    print(num1/num2)
    # print(a)
except ZeroDivisionError as e:
    print(e)
    print("Denominator cannot be zero")
else:
    print("This is else block")
finally:
    print("I will always get executed")
print(5+5)