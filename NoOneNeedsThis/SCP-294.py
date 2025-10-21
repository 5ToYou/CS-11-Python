import random

drinks = {}
health = 100
color_palette = ["red","orange","yellow","green","blue","purple","pink","white","black"]

def create_drink(drink_name):
    while True:
        color = input("color of your drink: ").lower()
        if color in color_palette:
            try:
                temp = float(input("drink temperature (in °C): "))
                glow = input("is drink glowing?(yes/no): ").lower() == "yes"
                break
            except ValueError:
                print(f"Invalid temperature. Please enter a numerical value.")
        else:
            print(f"color {color} dont exist")

    drinks[drink_name] = {
        "randomized": False,
        "color": color,
        "temperature": temp,
        "glow": glow,
    }
    print(f"drink '{drink_name}' created")

def create_random_drink(drink_name):
    temp = random.randint(1,140)
    glow = random.choice(["yes", "no"])
    color = random.choice(color_palette)
    
    drinks[drink_name] = {
        "randomized": True,
        "color": color,
        "temperature": temp,
        "glow": glow,
    }
    print(f"random drink '{drink_name}' created")

def acces_drink(choose):
    if choose in drinks:
        info = drinks[choose]
        print(f"drink: {choose}")

        if info["randomized"]:
            print("color: ?")
            print("temperature: ?")
            print("glowing: ?")
        else:
            print(f"color: {info['color']}")
            print(f"temperature: {info['temperature']} °C")
            print(f"glowing: {info['glow']}")
    else:
        print(f"there is no drink '{choose}' found")

def have_a_drink(choose,health):
    info = drinks[choose]
    temp = info["temperature"]
    if temp >= 100:
        print("You died from heavy burns")
        return 0
    elif temp >= 70:
        print("You got heavy injuries from that drink")
        return health - 50
    else:
        print("Yummy")
        del drinks[choose]
        return health

def is_alive(health):
    return health > 0
    
def menu():
    print("1 = show drinks")
    print("2 = acces drink")
    print("3 = add drink")
    print("4 = add random drink")
    print("5 = end program")

while True:
    
    if not is_alive(health):
        print("You are dead")
        break

    menu()
    while True:
        try:   
            choice = input("Enter what you want to do: ")
            break
        except ValueError:
            print(f"{choice} dont match")

    match choice:

        case "1":
            if not drinks:
                print("There is no drinks")
            else:
                print(f"Available drinks: {list(drinks)}")

        case "2":
            choose = input("choose drink you want: ")
            acces_drink(choose)
            if choose in drinks:
                drink_it = input("Want to drink it? (yes/no): ").lower()
                if drink_it == "yes":
                    health = have_a_drink(choose, health)
                else:
                    print("Your choice man...")
            else:
                pass

        case "3":
            drink_name = input("Enter drink name: ")
            create_drink(drink_name)

        case "4":
            drink_name = input("Enter drink name: ")
            create_random_drink(drink_name)

        case "5":
            print("Exit...")
            break

        case _:
            print(f"{choice} invalid")