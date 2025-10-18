import random

while True:
    slot1 = random.randint(1,9)
    slot2 = random.randint(1,9)
    slot3 = random.randint(1,9)



    print(f" = {slot1} {slot2} {slot3} = ")

    if slot1 == slot2 == slot3:
        print("  JACKPOT")
        break


    choice = input("Press Enter to roll: ")
    match choice:
        case "":
            pass
        
        case _:
            print("99.9% of gamblers quit before hitting big")
            break

    