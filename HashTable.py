import random

HashTable = [None,None,None,None,None,None,None,None]


def lengh():
    if len(HashTable) > 8:
        print("Cant add more than 8")
        HashTable.pop(8)

def insert(where,value):

    if not HashTable[where]:
        HashTable.insert(where,value)
    else:
        print("occupied")


def random_insert(value):
    r = random.randint(1,8)
    
    if not HashTable:
        print("occupied")
    else:  
        HashTable.insert(r, value)

def menu():
    print("1 = random add")
    print("2 = add")
    print("")

while True:
    print("Lengh of table:",len(HashTable))
    menu()
    print("HashTable is ",HashTable)
    choice = input("Enter func: ")
    match choice:

        case "1":
            value = input("Enter what to insert: ")
            random_insert(value)
            lengh()

        case "2":
            where = int(input("Where to insert: "))
            if where > 8:
                print("There is only 8 buckets")
            else:
                value = input("Enter what to insert: ")
                insert(where,value)

        case _:
            print("Exit")
            break
            
