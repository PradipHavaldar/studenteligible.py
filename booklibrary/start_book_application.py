

from booklibrary.book_info import Book
from booklibrary.book_service import BookService

def get_input_from_user():
    bid = int(input('Enter Book Id : '))
    bnm = input('Enter Book Name : ')
    baut = input('Enter Book Author : ')
    bprc = float(input('Enter Book Price : '))
    bqty = int(input('Enter Book Qty : '))
    #return Book(bid,bnm,baut,bprc,bqty)                                    #positional
    return Book(bkid=bid,bknm=bnm,bkaut=baut,bkpric=bprc,bkqty=bqty)        #named param

def add_book_input():
    book = get_input_from_user()                                           # input to append book
    service.add_book(book)


def delete_book_input():
    bkid = input('Enter Book Id for Delete : ')
    service.delete_book(bkid)

def update_book_input():
    print("Enter Data For Update Operation ")
    book = get_input_from_user()

def get_book_input():
    pass

def get_author_name_input():
    pass

def get_min_price_input():
    pass

def get_max_price_input():
    pass

if __name__ == '__main__':      # only if we execute the same module--> tabhi--> main condition--> execution hoga..
   # book = get_input_from_user()

   service = BookService()

   while True:

        print("""
            1. Add Book
            2. Get/Search Book
            3. Get All Books
            4. Delete Book
            5. Update Book
            6. Min Price
            7. Max Price
            8. Search By Author
        """)

        operations = {
                1: add_book_input,
                2: get_book_input,
                3: service.get_all_books,
                4: delete_book_input,
                5: update_book_input,
                6: get_min_price_input,
                7: get_max_price_input,
                8: get_author_name_input
        }
