import random

health = 100
limb1 = random.randint(1,5)

if limb1 == 5:
    limb2 = random.randint(1,4)
else:
    limb2 = random.randint(1,5)

damage = random.randint(10,30)

if damage == 30:
    damage = 50
    print("CRIT")

print(f"damage {damage}")

def limb_damage(limb):
    extra = 0
    if limb in (1, 2):
        print("You lost leg")
        extra = 10
    elif limb in (3, 4):
        print("You lost arm")
        extra = 10
    elif limb == 5:
        print("You lost head")
        extra = 80
    return extra

damage += limb_damage(limb1)
damage += limb_damage(limb2) 
        
        
if limb1 in range(1,3) and limb2 in range(1,3):
     print("WORLD CUTTING SLASH")
     damage += 20

elif limb1 in range(3,5) and limb2 in range(3,5):
     print("CLEAVE")
     damage += 20
     

health -= damage
print(f"Total damage: {damage}")
print(f"Your health: {health}")


if health <= -10:
    print("You got turned into dust")

elif health <= 0:
    print("You are dead")
else:
    print("I LEAVE")