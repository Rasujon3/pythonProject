books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn JAVA")
print(books)

books.pop()
print("Now the last book is : ",books[-1])

books.pop()
print("Now the last book is : ",books[-1])

books.pop()
if not books:
    print("No books left.")