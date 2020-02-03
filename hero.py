from random import *
from exceptions import *
import utils


class  Beast:
    def __init__(self, name):
        self.name = name
        self.health = 100   # Здоровье
        self.strength = 100 # Сила удара
        self.armor = 100    # Броня
        self.accuracy = 80  # Вероятность попадания по цели
        self.inheritance = []  # Вещи, которые останутся после смерти существа
        self.alive = True   

    def attack(self, enemy):
        enemy.attacked_by(self)

    def attacked_by(self, enemy):
        hurt = enemy.strength * random() - self.shield*random()
        if ( hurt > 0 ) :
            self.health -= hurt
        else:
            print(enemy.name, " промазал")

        if  self.health <= 0 : 
            self.alive = False
            self.die()

    def die(self):
        print("I am ", self.name,". My health is 0. I've died", sep='')


    def read_from_file(self, fileStream):
        for line  in fileStream:
            words = utils.split_by_words(line)
            if  not words : 
                continue
            if  words[0] == "#Name":
                self.name = " ".join(words[1:])
            elif  words[0] == "#Health":
                self.health = int(words[1])
            elif words[0] == "#Strength":
                self.strength = int(words[1])
            elif words[0] == "#Armor":
                self.armor = int(words[1])
            elif words[0] == "#Accuracy":
                self.accuracy = int(words[1])
            elif words[0] == "#Inheritance":
                self.inheritance.append( ( words[1], int(words[2]) ) )
            elif words[0] == "#EndBeast":
                return




class Character(Beast):
    def __init__(self, name):
        Beast.__init__(self, name)
        self.endurance = 30    # Выносливость (сколько веса может нести)
        self.cariedThings = [] # Список вещей с собой
        self.usedThings = []   # Список надетых вещей










