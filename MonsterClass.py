import random
class Monster(object):
    damage = random.randint(0,10)

    def __init__(self, damage, name):
         self.damageIndex = damage
         self.nameIndex = name

    def __str__(self)
