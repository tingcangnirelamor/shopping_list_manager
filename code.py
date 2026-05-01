try:
    with open("shopping_list.txt", "x") as f:
        f.write("Created new file successfully.")
        
except FileExistsError:
    print("File already exists.")

    with open("shopping_list.txt", "w") as f:
        f.write("Overwritten existing file.")

        while True:
            
            try:
                print("Menu")
                print("1. Add an item.")
                print("2. Change an item.")
                print("3. Remove an item.")    
                print("4. Exit.")

                choice = int(input("Enter a choice: "))
            
            except ValueError:
                    print("Enter a valid choice.")
            break
    
    while True:
        if choice == 1:
            itemlist = input("Enter an item: ")
            with open("shopping_list.txt", "a") as f:
                f.write(itemlist + "\n")
                break