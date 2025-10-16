import random

limb1 = random.randint(1,5)
limb2 = random.randint(1,5)

match limb1:

    case 1 | 2:
        print("You lost leg")
        
        
    case 3 | 4:
        print("You lost arm")    
        
    case 5:
        print("You lost head")   
        
match limb2:

    case 1 | 2:
        print("You lost leg")
        
        
    case 3 | 4:
        print("You lost arm")    
        
    case 5:
        print("You lost head")    
        
        
if limb1 in range(1,3) and limb2 in range(1,3):
     print("WORLD CUTTING SLASH")
 
if limb1 in range(3,5) and limb2 in range(3,5):
     print("How you suppose to cook now")
     
if limb1 == 5 and limb2 == 5: # type: ignore