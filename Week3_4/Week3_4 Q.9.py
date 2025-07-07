def get_book_details():
    books = []  # List to store book dictionaries

    for i in range(5):
        print("\nEnter details for Book ",i+1,": ")
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        cost = float(input("Cost: "))

        # Create dictionary for one book
        book = {
            "Title": title,
            "Author": author,
            "ISBN": isbn,
            "Cost": cost
        }

        # Add the book to the list
        books.append(book)

    return books

# Get books from user
book_list = get_book_details()

# Print all book details
print("\nBook Details:")
i = 1
for book in book_list:
    print("\nBook ",i,":")
    for key in book:
        print(key,": ", book[key])
    i += 1
