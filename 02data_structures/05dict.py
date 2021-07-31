#dictionary-> unorderd,mutable
# keys of dictionary can only be immutable datatypes
stu={
    "name":"John",
    "age": 13,
    "sub":['maths','sci']
}

# print(stu['age'])

stu['age']=15
# print(stu)

# print(stu.keys())
# print(stu.values())

# print(stu.items())

# for k,v in stu.items():
#     print(f"{k} --> {v}")

# stu['country']='IND'
# print(stu)

# stu.update({'country':'US'})
# print(stu)

# stu2=dict(**stu, marks=[1,2,2,5])
# print(stu2)

# print(stu['one'])
# print(stu.get('one','NA'))
print(stu)
# print(stu.pop('sub'))
# print(stu.clear())
del stu
print(stu)

