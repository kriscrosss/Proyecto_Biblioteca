from Libro import Libro
from Biblioteca import Biblioteca
from LibroDi import Ebook

def main_menu():
    b = Biblioteca()
    
    while True:
        print("""
--- Welcome to Biblioteca setso entre primos enanos haciendo ecuaciones con stephen hawking ---
              
[                --- Menu ---                ]             
1. Show available books
2. Delete book
3. Delete multiple books
4. Search Book
5. Modify book
6. Change format
7. Enter multiple books
8. Enter new book
0. Exit""")

        opc = str(input("Choose an option: "))

        if opc == "1":
            b.imprimir_libros()
            input("To return press enter")

        if opc == "2":
            b.eliminar_libro()
            
        if opc == "5":
            b.modificar_libro()

        if opc == "8":
            print("Enter the information of the new book(If the book is digital, enter the format and size)")
            btype = input("¿The book is digital? (Y/N)")
            if btype.upper() == "Y": 
                name = input("Name: ")
                autor = input("Autor: ")
                edit = input("Editorial: ")
                year = input("Year: ")
                genre = input("Genre: ")
                pages = input("Pages: ")
                format = input("Format: ")
                size = input("Size: ")
                
                db = Ebook(name,autor,edit,year,genre,pages,format,size)
                b.agregar_libro(db)
            else:
                name = input("Name: ")
                autor = input("Autor: ")
                edit = input("Editorial: ")
                year = input("Year: ")
                genre = input("Genre: ")
                pages = input("Pages: ")
            
                nb = Libro(name,autor,edit,year,genre,pages)
                b.agregar_libro(nb)
            print("Book added successfully")
            input("To return press enter")

        if opc == "0":
            print("Goodbye MALDITO, TONTO, HEDIONDO A PEO, FEo")
            break

main_menu()

