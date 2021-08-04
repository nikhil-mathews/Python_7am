import simple
import complex

# print(simple.add(1,2))
# print(complex.cube(2))
# print(complex.add(5))



# from complex import cube,add
# from simple import add

# print(add(1))

print(__name__)

def main():
    print("Executing main function")
    print(complex.sqr(2))
    print(simple.mul(3,4))


if __name__ == '__main__':
    main()