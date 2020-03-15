import random

# Main

global Health
global name
global Monsters
global traps
global treasureNum
global treasures
treasureNum=0

def intro():
    
    name = str(input("Enter your character name: "))
    print(f"The Mighty {name} has entered the Labyrinth ....")
    print(f"The Labyrinth is filled with danger, prepare your self OR DIE !!!!!")
#def ending():
    

def monsters(Health):
    Monsters = []
    Monsters.append("Tim the Enchanter")
    Monsters.append("the Wolf Man")
    Monsters.append("a Gremlin")
    Monsters.append("a Goblin ")
    Monsters.append(" aDragon Hatchling")
    Monsters.append("a Skeleton")
    Monsters.append("an Ancient Automaton")
    
    print(" Oh NO! You Have encountered")
    
    X = random.randint(0,100)
    if( X>=0 and X<=4):             
        print(Monsters[0])
        Health=Health-Health
    elif( X>=5 and X<=15):
        print(Monsters[1])
        Health=Health-15
    elif( X>=16 and X<=36):
        print(Monsters[2])
        Health=Health-5
    elif( X>=37 and X<=55):
        print(Monsters[3])
        Health=Health-5
    elif( X>=56 and X<=70):
        print(Monsters[4])
        Health=Health-15
    elif( X>=71 and X<=88):
        print(Monsters[5])
        Health=Health-5
    elif( X>=89 and X<=100):
        print(Monsters[6])
        Health=Health-20

    #if(Health>0):
        #print("You managed to escape the monster but have been wounded along the way")
        #print("Health = ")
        #print(Health)
        #return Health
def Traps(Health):
    traps=[]
    traps.append("Bottomless pit")
    traps.append("Poison dart trap")
    traps.append("Spike trap")
    traps.append("A fucking Rue Goldberg Machine!")
    print(" Oh NO! You Have encountered")
    Y = random.randint(1,4)
    if(Y==1):             
        print(traps[0])
    elif( Y==2):
        print(traps[1])
    elif(Y==3):
        print(traps[2])
    elif(Y==4):
        print(traps[3])
        return Health
    print("You manage to survive and find ")
#def treasures():
    #treasures=[]
    #treasures.append("Holy Grail")
    #treasures.append("Sword of Damocles")
   # treasures.append("Ark of the Covenant")
    #a= random.randint(0,9)
   # if(a>=0 and a<=3):
    #    print(treasures[0])
    #elif(a>=4 and a<=6):
     #   print(treasures[1])
    #elif(a>=7 and a<=9):

    #    print(treasures[2])
    
    
def Obstacle(Health, treasureNum):
    Z= random.randint(0,6)
    if(Z>=0 and Z<=3):
        monsters(Health)
        return Health-5
    elif(Z>=4 and Z<=6):
        Traps(Health)
        return Health
   # elif(Z>=7 and Z<=9):
    #    treasures()
     #   return treasureNum+1
     
def NewRoom(Health, treasureNum):
    choose = int(input("You must choose a Path at a fork in the labrinyth, at your own risk (hit 1 or 2): "))
    
    if (choose==1):
        print("you go down the first path and enetr a room ...")
        Obstacle(Health, treasureNum)
        return treasureNum
    elif (choose==2):
        print("you go down the second path and enter a room ...")
        Obstacle(Health, treasureNum)
        return treasureNum
intro()
Health=100
while(treasureNum<3):
    NewRoom(Health, treasureNum)
    treasures=[]
    treasures.append("Holy Grail")
    treasures.append("Sword of Damocles")
    treasures.append("Ark of the Covenant")
    a= random.randint(0,25)
    if(a>=0 and a<=3):
        print(treasures[0])
        treasureNum+=1 
    elif(a>=4 and a<=6):
        print(treasures[1])
        treasureNum+=1 
    elif(a>=7 and a<=9):
        print(treasures[2])
        treasureNum+=1
    elif(a>=10 and a<=25):
        print("Nothing")
    print(treasureNum)
print("Yout managed to survive the labrinyth and return with the treasure, Well done!")    
