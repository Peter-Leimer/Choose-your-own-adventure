import random

# Main
#Intro
global Health
global name
global Monsters
global traps
global treasureNum
global treasures
treasureNum=0

def intro():
    Health=100
    name = str(input("Enter your character name: "))
    print(f"The Mighty {name} has entered the Labyrinth ....")
    print(f"The Labyrinth is filled with danger, prepare your self OR DIE !!!!!")


def monsters():
    Monsters = []
    Monsters.append("Tim the Enchanter")
    Monsters.append("Wolf Man")
    Monsters.append("Uruk hai")
    Monsters.append("Gremlin")
    Monsters.append("Goblin ")
    Monsters.append("Dragon Hatchling")
    Monsters.append("Skeleton")
    print(Monsters[0])
    print(Monsters[1])
    print(Monsters[2])
    print(Monsters[3])

def Traps():
    traps=[]
    traps.append("Bottomless pit")
    traps.append("Poison dart trap")
    traps.append("Spike trap")
    traps.append("A fuking Rue Goldberg Machine, with FIRE!")
    
def treasures():
    treasures=[]
    treasures.append("Holy Grail")
    treasures.append("Sword of Damocles")
    treasures.append("Ark of the Covenant")

def NewRoom():
    choose = int(input("You must choose a Path at a fork in the labrinyth, at your own risk (hit 1 or 2)"))
    if (choose==1):
        print("path1")
    elif (choose==2):
        print("path2")

intro()
NewRoom()
#monsters()
