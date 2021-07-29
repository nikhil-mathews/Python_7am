# list 
# heterogeneous
# ordered
# mutable--> they can be changed

nums=[1,2,3,4,5,6]


# indexing
# print(nums[0])
# nums[0]=11

# print(nums[0])
# print(nums[-1])
# print(len(nums))


# TODO: slicing
# list_name[start_index:end_index+1:jump]

# print(nums[::])
# print(nums[:3])
# print(nums[-5:-1])
# print(nums[::-1])
# print(nums[::2])

# TO ADD ONE WLWMENT AT A TIME
# nums.append(99)
# print(nums)

# TO ADD MULTIPLE ELEMENTS
# nums.extend([33,4,55])
# print(nums)


# TODO: Creating a custom list

# s=int(input("Enter size of list: "))
# vals=[]

# for i in range(s):
#     x=int(input("Enter an element :"))
#     vals.append(x)
# else:
#     print("Listcreated successfully!!")
#     print(vals)

a=[11,1,3,45,64]
# print(a.count(11))

# print(a.index(11))
# a.insert(0,99)
# print(a)

# while 11 in a:
#     a.remove(11)
# else:
#     print(a)

# TODO: sorting
# a.sort()
# print(a)
# a=sorted(a,reverse=True)
# print(a)

# TODO: reversing
# a.reverse()
# print(a)

print(sum(a))
print(min(a))
print(max(a))