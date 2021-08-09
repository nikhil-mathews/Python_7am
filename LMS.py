class Library:

    books = ["Book_"+str(i+1) for i in range(10)]

    d={}

    def addb(self,b: str):

        self.books.append(b)

    def removeb(self,b,student):

        if b not in self.books: print("Book unavailable")

        else:

            self.books.remove(b)

            self.d[b] = student

            print(b+" removed")

    def returnb(self,b):

        if b not in self.d.keys(): print("Book not taken from this library")

        else:

            self.books.append(b)

            del self.d[b]

            print("Book returned and owed books updated")

   

lib = Library()

All_students = {}

class student:

    def __init__(self,name, roll, age):

        self.name = name

        self.roll = roll

        self.age = age

       

    def addto(self):

        All_students[self.roll] = self

   

 

student('Ali',2355,21).addto()

student('kia',6321,35).addto()

student('foa',3452,52).addto()

 

 

print('1.Add book\n2.Take book\n3.Return book\n4.View available books\n5.Owed books\n6.Exit\n')

while True:

    n=int(input('Choose option: '))

    if n == 1:

        lib.addb(input('Give title: '))

        print("Book added")

    elif n == 2:

        roll = int(input('Student roll: '))

        if roll not in All_students.keys():

            print('Invalid roll number')

        else: lib.removeb(input('Book Title: '),All_students[roll])

    elif n == 3:

        roll = int(input('Student roll: '))

        if roll not in All_students.keys():

            print('Invalid roll number')

        else:

            book = input('Book Title: ')

            if lib.d[book].roll==roll: lib.returnb(book)

            else: print(book+" was borrowed by "+lib.d[book].name)           

    elif n == 4:

        print(lib.books)

    elif n ==5:

        print('\n'.join([str(book)+' : '+str(lib.d[book].name) for book in lib.d]))

    elif n ==6:

        break

    else:

        pass