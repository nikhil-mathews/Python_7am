'''
base case
simpler problem of complex problem

'''

# add first 5 nums
# 1+2+3+4+5

# 1+2=3
# 3+3=6
# 6+4=10
# 10+5=15

def add(num):
    # base case
    if num==1:
        return 1
    
    return num + add(num-1)

print(add(5))


