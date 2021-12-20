



#what book means -->
class Book:

    def __init__(self,bkid,bknm,bkprc,bkauth,bkpubl):
        self.bookId = bkid
        self.bookName = bknm
        self.bookPrice = bkprc
        self.bookAuthor = bkauth
        self.bookPublication = bkpubl

    #single object--> representation --> Str
    def __str__(self):  # str is method--> which represents to the object--> book object-> instead printing memory addresses-->
        return f'''\n Book Id :{self.bookId} BookName :{self.bookName} BookPrice :{self.bookPrice} BookAuthor :{self.bookAuthor} BookPublication :{self.bookPublication}'''

    # collection / group of objects ka--> contents printing..
    def __repr__(self):
        return str(self)



def get_input_from_user():
    count = int(input('Enter Book Id : '))           #int
    bknm = input('Enter Book Name : ')              #str
    bkau = input('Enter Book Author : ')            #str
    bkpub = input('Enter Book Publication : ')      #str
    bkpri = float(input('Enter Book Price : '))     #float
    return Book(count,bknm,bkpri,bkau,bkpub)


library = []

def add_books():
    while True:
        book = get_input_from_user()
        library.append(book)
        choice = input('Do you want to continue [y/n/Yes/No] : ')
        while choice.lower() not in ['y','n','yes','no']:
            choice = input('Do you want to continue [y/n/Yes/No] : ')    # by intension --> bymistake  --> not aware
        if choice.lower() in ['n','no']:
            break


def remove_book_v2():
    bkid = int(input('Enter Book Id : ')) #[101,102,103]--> 110
    for book in library:
        if book.bookId == bkid:
            library.remove(book)
            print('Book Removed')
            return                          # directly function ko hi stop karega

    print(f'Book with Given Id {bkid} Not Found so cannot delete')

def search_book():
    bkid = int(input('Enter Book Id : '))
    for book in library:
        if book.bookId == bkid:
            return book

    print(f'Book with Given Id {bkid} Not Found ')


def show_all_books():
    if library:
        print(library)
    else:
        print("No Books in library currently...!")


#services -->
def get_max_price_book():
    pass

def get_min_price_book():
    pass

def get_total_book_price():
    pass

def avg_book_price():
    pass

def search_by_author_name():
    pass

if __name__ == '__main__':
    while True:
        print(''' 
        -----------------------------------------------------
            Select Your Choice : 
                1. Add Book 
                2. Remove Book
                3. Search Book
                4. Show All Books
        ''')
        choice = int(input('Enter Your Choice : '))
        operations = {
            1 : add_books,
            2 : remove_book_v2,
            3 : search_book,
            4 : show_all_books
        }
        funref = operations.get(choice)         # kind of switch --> switch -condition are not given .
        if funref:
            ans = funref()
            if ans:
                print(ans)
        else:
            print('INvalid CHoices..')


import sys
sys.exit(0)
if __name__ == '__main__':
    while True:
        print(''' 
        -----------------------------------------------------
            Select Your Choice : 
                1. Add Book 
                2. Remove Book
                3. Search Book
                4. Show All Books
        ''')
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            add_books()
        elif choice == 2:
            remove_book_v2()
        elif choice ==3:
            book = search_book()
            print(book)
        elif choice == 4:
           show_all_books()
        else:
            print('Invalid Choice..!')







'''
import sys
sys.exit(0)
while True:
    book = get_input_from_user()
    library.append(book)
    count = 0
    for item in range(3):
        choice = input('Do you want to continue : ')
        if choice.lower() in ['n','no']:            #NO     no      n   --> yes --> YES yes Yes yES --
            count = 3
            break
        elif choice.lower() in ['y','yes']:                     #ABCD
            break
        else:
            print('Invalid Choice')
            count = count + 1
            if count==3:
                print('Number of attempts exceeds : --> program will be stopped..')
    if count==3:
        break  # while ko
print(library)
'''
import sys
sys.exit(0)
for item in range(2):                          #10 times
    bk = get_input_from_user()                  #10 times --> will cal to the getinput --> bookinfo--10time--< book
    library.append(bk)

print(library)
def remove_book_v1():
    bkid = int(input('Enter Book Id : ')) #[101,102,103]--> 110
    isBookDeleted = False
    for book in library:
        if book.bookId == bkid:
            library.remove(book)
            isBookDeleted = True            #actual mein book remove hoga --> isBookDeleted
            break

    if isBookDeleted:               #False/True
        print('Book Removed From Library...!')
    else:
        print('Given id book Not present -- so cannot delete..')



empid  = int(input('Enter Employee Id : '))
empName = input('Enter Employee Name : ')
empSalary = float(input('Enter Employee Salary :'))

stat1 = "Employee id is 101 and name is Yogesh, takes salary 10000.0"  #dyanically


#string formatting -> diff

stat1 = "Employee id is {} and name is {}, takes salary {}".format(empid,empName,empSalary) #position+seq+num of
print(stat1)
stat1 = "Employee id is {1} and name is {0}, takes salary {2}".format(empName,empid,empSalary)
print(stat1)
stat1 = "Employee id is {b} and name is {c}, takes salary {a}".format(a=empSalary,b=empid,c=empName)
print(stat1)
#python 3.6 --> easiest way..
stat1 = f"Employee id is {empid} and name is {empName}, takes salary {empSalary}"
print(stat1)


import sys
sys.exit(0)
