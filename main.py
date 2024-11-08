def load_data(title):
  pass

#Create Book class
class Book:
  #Provide attributes
  def __init__(self, title, author, pages):
  #Constructor to initialize
    self.title = title
    self.author = author
    self.pages = pages
    self.data = load_data(title)
    self.read = False

  #Define description() method
  def description(self):
    #Return string
    return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
  #Define marked_as_read() method
  def marked_as_read(self):
    #Set read to True
    self.read = True
    #Print message
    print(f"{self.title} by {self.author} has been read.")

#Create book object 1
book1 = Book("Becoming Supernatural: How Common People Are Doing the Uncommon", "Dr. Joe Dispenza", 384)
#Print description
print(book1.description())
#Mark as read
book1.marked_as_read()

#Create book object 2
book2 = Book("The Seven Spiritual Laws of Success: A Practical Guide to the Fulfillment of Your Dreams", "Deepak Chopra", 118)
#Print descriptions=
print(book2.description())

#Create User class
class User:
  #Provide attributes
  def __init__(self, name, accnt):
    #Constructor to initialize
    self.name = name
    self.accnt = accnt
    self.shelf = []
    self.balance = 0

  #Define buy_book
  def buy_book(self, book):
    self.book += book1[book] and book2[book]
    self.shelf += Book(book1 and book2)

  #Define read_book
  def read_book(self, book):
    book = self.shelf[self.shelf.find(book)]