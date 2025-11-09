from abc import ABC,abstractmethod
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=True

    @abstractmethod
    def borrow(self):
        pass
    @abstractmethod
    def return_book(self):
        pass

class PhysicalBook(Book):
    def borrow(self):
        if self.available:
            self.available=False
            print(f"{self.title} is borrowed")
    def return_book(self):
        self.available=True
        print(f"{self.title} is returned")

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=[]
    def borrow_book(self,book):
        book.borrow()
        if not book.available:
            self.borrowed_books.append(book)
    def return_book(self,book):
        book.return_book()
        self.borrowed_books.remove(book)
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_book(self,book):
        self.books.append(book)
    def add_member(self,member):
        self.members.append(member)
    def show_available_books(self):
        print("\n----Available Books----")
        for book in self.books:
            if book.available:
               print(f"[{book.title}] by {book.author}")

#MAKE A LIBRARY,BOOK AND MEMBER OBJECT
library1=Library()
b1=PhysicalBook("Twiga the honey","Abdirahman Ahmed",1234567)
b2=PhysicalBook("Blabla","Abdullahi Yussuf",233445)
m1=Member("Ayaan Ahmed","m001")

library1.add_book(b1)
library1.add_book(b2)
library1.add_member(m1)
library1.show_available_books()
m1.borrow_book(b1)
library1.show_available_books()
m1.return_book(b1)
library1.show_available_books()