Books = {
        "Books":["Wind in the Willows","The Seventh Shadow",
                  "The monk whold soold is ferrari"]}
def add ():
    a = int(input("How many books to add = "))
    for i in range(a):
        Books[i] = input("Enter the Book name = ")