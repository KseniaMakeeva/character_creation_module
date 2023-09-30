from random import randint

DEFAULT_ATTACK = 5

DEFAULT_DEFENCE = 10

class Character:

RANGE_VALUE_ATTACK = (1, 3)

RANGE_VALUE_DEFENCE  = (1, 5)
    def __init__(self, name):
        self.name = name


    def attack(self):
        value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')


    def defence(self):
        ...


    def special(self):
        ...


class Warrior(Character):
    
    ...

class Mage(Character):
    
    ...

class Healer(Character):
    
    ...