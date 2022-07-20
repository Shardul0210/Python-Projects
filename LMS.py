class Library:

    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def displayAvailableBooks(self):
        print("The books present in this Library are")
        for book in self.books:
            print(" *" + book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        elif bookName=="":
            print("Enter a valid name")
        else:
            print("Sorry,this book is either not available or has been issued to someone else.Please wait until the book is returned")
    def returnBook(self,bookName):
        if bookName=="":
            print("Enter a valid name")
        else:
            self.books.append(bookName)
            print("Thanks for returning this book.Hope you enjoyed this book.Have a great day")
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow:")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to add or return:")
        return self.book

if __name__=="__main__":
    centralLibrary=Library(["H.K.Das","Bransden","Wiley","D.C.Tayal","Liboff","Wahab"])
    # centralLibrary.displayAvailableBooks()
    student=Student()
    while(True):
        welcomeMsg='''\n=====Welcome to Central Library=====
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the library
        '''
        print(welcomeMsg)
        a=int(input("Enter a choice number"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library")
            exit()
        else:
            print("Invalid choice")
       