from abc import ABC, abstractmethod

class BookAdditionStrategy(ABC):
    @abstractmethod
    def add_book(self):
        pass

class ExcelBookAdditionStrategy(BookAdditionStrategy):

    @staticmethod
    def add_book(excel_file_path):
        '''
        #parse excel file to get data
        book_data = parse(excel_file)
        #add a check to see if it is a new book or a new book copy
        for data in book_data:
            isbn = data[0]
            if isbn not in BooksTable:
                NewBookAdditionStrategy.add_book() # total_copies here would be one
            else:
                BookCopyAdditionStrategy.add_book(isbn)

        '''
        pass

class NewBookAdditionStrategy(BookAdditionStrategy):

    @staticmethod
    def add_book(self, title, language, author, isbn, price, version, publication_info, book_type, genre, total_copies):
        #create book object and add it to books table
        #update BookTitle Table since its a new book
        #update BookCopyTable as well
        for _ in range(total_copies):
            BookCopyAdditionStrategy.add_book(isbn)
            pass
        

class BookCopyAdditionStrategy(BookAdditionStrategy):

    @staticmethod
    def add_book(self, isbn):
        #add book to the BookCopy Table
        #need not update the book copy history table
        pass

    



