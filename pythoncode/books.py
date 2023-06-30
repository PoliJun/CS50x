books=[]

# Add three books to your shelf
for i in range(3):
    book=dict()
    book['title']=input("Enter title of book: ").strip().Capitalize()
    book['author']=input("Enter author of book: ").strip().Capitalize()
    
    books.append(book)
    
for book in books:
    print(book['title'])