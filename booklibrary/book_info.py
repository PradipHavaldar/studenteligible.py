


class Book:

    def __init__(self,bkid,bknm,bkaut,bkpric,bkqty=1):      #default param
        self.bookId = bkid
        self.bookName = bknm
        self.bookPrice = bkpric
        self.bookQty = bkqty
        self.bookAuthor = bkaut

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)






b2 = Book(101,'AAAA','MR YYY',2893.34,2)
print(b2)  # contents --> based on eq method -->eq is not defined here--> object la eq--> is [ref]



