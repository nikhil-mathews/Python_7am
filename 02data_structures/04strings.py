'''
format of strings
'''

# n1=2
# n2=3
# sum=n1+n2

# print(str(n1) + "+" +str(n2)+ "=" + str(sum))

# print("{0}+{1}={2}".format(n1,n2,sum))

# print(f"{n1} + {n2} ={sum}")


'''
strings-> ordered, immutable
'''
s="python"

# print(len(s))
# print(s[0])
# print(s[-1])

# Not applied
# s[0]="P"
# print(s)


# TODO: slicing
# print(s[1:5])
# print(s[1:5:2])

# print(s[::-1])

# print(s.count('o'))

# print(s.find('p',3))
# print(s.index('P'))

# print(s.startswith('py'))
# print(s.endswith('py'))

# print(s.upper())
# print(s.lower())
# print(s.title())

# validatior
s="python12"
# print(s.islower())
# print(s.isalpha())
# print(s.isalnum())
# p="   "
# print(p.isspace())

# TODO: strip

# p="       pass           "
# print(p.strip())
# print(p.lstrip())
# print(p.rstrip())


# TODO: split
# s="we are learning python"
# print(s.split(' ',2))
# print(s.split('a'))

# s=input("Enter nums").split(" ")
# print(s)


# TODO: join
# uname=(".").join(['ram','sharma'])
# domain='abc.com'
# email='@'.join([uname,domain])
# print(email)


# TODO: replace
s="python12oooo"
# s=s.replace('o','@',2)
# print(s)

# print(ord('a'))
# print(ord('A'))

# print(chr(87))
# print(max(s))
# print(min(s))

# escape sequences
'''
\n-> new line
\t-> tab
\b-> backspce
\a-> alert
'''
path=r"C:\newfolder\tmp"
print(path)