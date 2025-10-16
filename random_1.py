import random

health = 100
limb1 = random.randint(1,5)
limb2 = random.randint(1,5)
damage = random.randint(10,30)

if damage == 30:
    damage = 50
    print("CRIT")

match limb1:
    case 1 | 2:
        print("You lost leg")
        damage += 10
    case 3 | 4:
        print("You lost arm")
        damage += 10    
    case 5:
        print("You lost head")   
        damage += 80
        
match limb2:
    case 1 | 2:
        print("You lost leg")
        damage += 10
    case 3 | 4:
        print("You lost arm")
        damage += 10      
    case 5:
        print("You lost head")
        damage += 80
    case 6:
        print("miss")  
        
        
if limb1 in range(1,3) and limb2 in range(1,3):
     print("WORLD CUTTING SLASH")
     damage += 20
 
elif limb1 in range(3,5) and limb2 in range(3,5):
     print("How you suppose to cook now")
     damage += 20
     
if limb1 == 5 and limb2 == 5:
    limb1 = 5
    limb2 = 6

health -= damage
print("Your health 100")
print(f"Total damage {damage}")


if health <= -10:
    print("You got turned into dust")
    
elif health <= 0:
    print("You are dead")

elif health >= 1:
    print("I LEAVE")