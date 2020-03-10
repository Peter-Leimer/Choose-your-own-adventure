# Main
#Intro
global Health
global name
global Monsters
global traps

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
    print(Monsters[0])
    print(Monsters[1])
    print(Monsters[2])
    print(Monsters[3])

def Traps():
    traps=[]
    traps.append("bottomless pit")

intro()
monsters()
