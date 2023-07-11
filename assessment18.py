class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return f"{self.title} by {self.author} ISBN{self.ISBN}"
books = []

with open('book.txt', 'r') as f:
    read_books = f.readlines()
    for b in read_books:
        title, author, ISBN = b.strip().split(',')
        my_book = Book(title.strip(), author.strip(), ISBN.strip())
        books.append(my_book)

for book in books:
    print (book)