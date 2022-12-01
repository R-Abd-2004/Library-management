client_list = ["Abdelrahman", "Sead", "khaled", "Hakem"]

books_list = ["Anna Karenina","The Great Gatsby","The Last Battle","Invisible Man","Don Quixote"]

borrowed_orders_list = ["Anna Karenina", "Invisible Man"]


#==============================================================================================================================

isAccountExist = input("Do You Have Acount? (Yes/No) ")

if isAccountExist == "Yes".lower():
    name = input("Enter Your Name: ")

    if name in client_list:
        print(f"== Welcome in our Library")

    else:
        print("You Are Not In The Client List")

        exit()

elif isAccountExist == "No".lower():
    create_account = input("Do You Want Create Account (Yes/No): ")

    if create_account == "Yes".lower():
        name = input("Enter Your Name: ")

        client_list.append(name)

        print("You Are Added To The Client List")

    elif create_account == "No".lower():
        print("Signed Out")

        exit()

    else:
        print("You must answer with yes or no")

        exit()


else:
    print("You must answer with yes or no")

    exit()


#==============================================================================================================================


class Client:

    def __init__(self, list_of_names):
        
        self.clients_names = list_of_names

    def requestBook(self):

        print("Enter the name of the book you'd like to borrow: ")

        self.book=input()

        return self.book

    def returnBook(self):

        print("Enter the name of the book you'd like to return: ")

        self.book=input()

        return self.book


#==============================================================================================================================


class Library:

    def __init__(self,list_of_books):

        self.available_books = list_of_books

    def display_all_books(self):

        print("The books we have in our library are as follows: ")

        print("================================")

        for book in self.available_books:

            print(book)

    # def lendBook(self,requestedBook):

    #         if requestedBook in borrowed_orders_list:

    #             print("Sorry the book you have requested is currently not in the library")

    #         else:

    #             print("The book you requested has now been borrowed")

    def lendBook(self,requestedBook):

        if requestedBook in self.available_books:

                print("The book you requested has now been borrowed")

                self.available_books.remove(requestedBook)
                
                borrowed_orders_list.append(requestedBook)

        else:

                print("Sorry the book you have requested is currently not in the library")

    def addBook(self,returnedBook):

            if returnedBook in books_list:

                self.available_books.append(returnedBook)

                print("Thanks for returning your borrowed book")

            else:

                print("You don't requested this book from her")

#==============================================================================================================================

class Main:

    client_list = Client(["Abdelrahman", "Sead", "khaled", "Hakem"])

    books_list = Library(["Anna Karenina","The Great Gatsby","The Last Battle","Invisible Man","Don Quixote"])
    
    borrowed_orders_list = ["Anna Karenina", "Invisible Man"]

    done=False

    while done==False:

        print(""" ======LIBRARY MENU=======
                1. Display all available books
                2. Request a book
                3. Return a book
                4. Exit
                """)

        choice=int(input("Enter Choice:"))
        
        if choice==1:

                    books_list.display_all_books()

        elif choice==2:

                    books_list.lendBook(client_list.requestBook())

        elif choice==3:

                    books_list.addBook(client_list.returnBook())

        elif choice==4:

                break

Main()