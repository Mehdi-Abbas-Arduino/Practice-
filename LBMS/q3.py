Books = {
    "Novels": ['Wind in the Willows', "George and The Marvelous Medicine"],
    "Science": ['Physics Matter']
}

def add_Books():
    a = int(input("Enter the number of books: "))
    for i in range(a):
        book_type = input("Is it a Novel (N) or Science (S) book? ").upper()
        if book_type == 'S':
            book_name = input("Enter the name of the Science book: ")
            Books["Science"].append(book_name)  # Correctly append the new book to the list
        elif book_type == 'N':
            book_name = input("Enter the name of the Novel: ")
            Books["Novels"].append(book_name)  # Correctly append the new book to the list
        else:
            print("Invalid type! Please enter 'N' for Novel or 'S' for Science.")

def remove_Books():
    remove = int(input("How many books to remove: "))
    for i in range(remove):
        book_name = input("Enter the name of the book to remove: ")
        found = False
        for category, book_list in Books.items():
            if book_name in book_list:
                book_list.remove(book_name)
                print(f"Removed '{book_name}' from {category} books.")
                found = True
                break
        if not found:
            print(f"Book '{book_name}' not found in the collection.")


print(Books)
borrowed = []
def borrow():
    number = int(input("Enter the number of books = "))
    book = input("Which book you want to borrow = ")
    for i in range(number):
        for index,value in Books.items():
            if book in value :
                print("You Can borrow it.")
                borrowed.append(book)
                Books[index].remove(book)
            
def returning_book():
    book = input("Which book you want to return = ")
    check = input("Was it a Novel type (N) Was it a Science book type (S) ").upper()
    for index,value in Books.items():
        if check == 'N':
            Books['Novels'].append(book)
        if check == 'S':
            Books["Science"].append(book)
    borrowed.remove(book)
    
