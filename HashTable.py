size = 8
HashTable = [None] * size



def hash_func(value):
    return sum(ord(c) for c in value) % size

def insert(value):
    index = hash_func(value)

    if HashTable[index] is None:
        HashTable[index] = value
        print("")
        print(f"Inserted '{value}' at {index}")
        return

    print("")
    print(f"Collision at {index}, looking for next...")
    original_index = index

    while True:
        index = (index + 1) % size

        if HashTable[index] is None:
            HashTable[index] = value
            print("")
            print(f"Inserted '{value}' at {index}")
            return

        if index == original_index:
            print("")
            print("HashTable is full! Can't insert more.")
            return
        
def expand():
    global HashTable, size
    size += 1
    HashTable = [None] * size
    print("")
    print("expanded by 1")
    print("")


def menu():
    print("1 = add")
    print("2 = ")
    print("3 = ")
    print("4 = expand")

while True:
    print("Lengh of table:",len(HashTable))
    menu()
    print("HashTable is ",HashTable)
    choice = input("Enter func: ")
    match choice:

        case "1":
            value = input("insert: ")
            insert(value)

        case "4":
            expand()

        case _:
            print("Exit")
            break
            
