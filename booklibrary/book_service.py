#service --> what are all options that we are offering to the end user...

from booklibrary.book_info import Book

class BookService:

    library = []                                #class level --> variable -> class name

    def add_book(self,book_info:Book):          #type(book_info) == Book
        if type(book_info) == Book:
            if book_info.bookId<=0:
                print('Invalid Book Id : ')
            elif book_info.bookPrice<=0:
                print('Invalid Book Price ')
            elif book_info.bookQty<=0:
                print('Invalid Book Qty ')
            elif len(book_info.bookName)<=1 or len(book_info.bookAuthor)<=1:                #check length of string book name and author
                print('Invalid Book Name/Author Name')
            else:
                BookService.library.append(book_info)                                       #library.list mdhe book append
                print('Book Successfully Added')
        else:
            print('Invalid Book Type...')

    def delete_book(self,bkid:int):
        isBookDeleted = False
        if type(bkid)==int:
            for book in BookService.library:
                if book.bookId == bkid:
                    BookService.library.remove(book)
                    isBookDeleted = True
                    break
        if isBookDeleted:
            print(f'Book {bkid} Successfully Deleted')
        else:
            print('Book Id is Invalid So cannot delete')

    def search_book(self,bkid:int):
        isElse = False
        if type(bkid) == int and bkid>0:
            for book in BookService.library:
                if book.bookId == bkid:
                   return book
        else:
            print('Invalid Book Id')
            isElse =True

        if not isElse:
            print('Book Not Found')

    def update_book(self,bkid:int,new_book_info:dict):  #reading k liye --> isko value kuch bh
        if type(bkid)==int and bkid>0:          #bt yanha fail
            if type(new_book_info) == Book:
                for book in BookService.library:
                    if book.bookId == bkid:
                        if new_book_info.get('name') and len(new_book_info.get('name'))>1:
                            book.bookName = new_book_info.get('name')

                        if new_book_info.get('price') and new_book_info.get('price')>0:
                            book.bookPrice = new_book_info.get('price')

                        if new_book_info.get('qty') and new_book_info.get('qty')>0:
                            book.bookQty = new_book_info.get('qty')

                        if new_book_info.get('author') and len(new_book_info.get('author'))>1:
                            book.bookAuthor = new_book_info.get('author')

                        print('Book Successfully Updated...')
                        return
            else:
                print("Invalid Book Type")
        else:
            print('Invalid Book Id..:')
    def get_all_books(self):
        return BookService.library      # library k andar hi all books

    def get_author_specific_books(self,author_name):
        author_books = []
        for book in BookService.library:
            if book.bookAuthor == author_name:
                author_books.append(book)

        if author_books:
            return author_books
        else:
            print('None of the Book found for this Author...')

    def get_max_or_min_price_book(self,max_value=True):
        book_val = None
        if BookService.library:
            if max_value:
                max_price = 0
                for book in BookService.library:
                    if book.bookPrice>max_price:
                        max_price = book.bookPrice
                        book_val = book
            elif BookService.library:
                min_price = BookService.library[0].bookPrice
                for book in BookService.library:
                    if book.bookPrice<min_price:
                        min_price = book.bookPrice
                        book_val = book

            return book_val
        else:
            print('No Book Present So cannot fetch min/max price..')


