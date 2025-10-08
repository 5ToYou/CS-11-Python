
print("Hello im gonna try things!")


def menu():
    print("")
    print("Add = 1")
    print("delete = 2")
    print("sort = 3")
    print("merge = 4")

value = None

def func():
    global listok
    listok = []
    return listok


def insert(listok, value):
    listok.append(value)
    return listok


main_list = func()

while True:
    menu()
    print(main_list)
    choice = input("Choose func: ")

    if choice == "1":
        value = input("What add: ")
        insert(main_list, value)

    elif choice == "2":
        if value in listok:
            listok.pop(0)
            print("item deleted")
        else:
            print("no value")
        
    elif choice == "3":
        main_list.sort()
        print("List sorted")

    elif choice == "4":
        pass

    else:
        break


print("You skipped")
