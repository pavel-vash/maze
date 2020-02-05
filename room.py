from exceptions import *
from random import *
from hero import Beast
import utils

allDirections = ["left", "right", "back", "front" ]
oppositeDirections = {"left": "right", "right": "left", "back": "front",
                      "front": "back"}

class Wall:
    def __init__ (self):
        pass



class Door(Wall):
    def __init__(self, state):
        self._state = state 


    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state


class PossibleBeast:
    def __init__(self, beast,  probability = 0):
        self.beast = beast
        self.appearanceProb = probability

class PossibleThing:
    def __init__(self, thing, probability = 0):
        self.thing = thing
        self.appearanceProb = probability


class Room:
    def __init__(self, allBeasts = {}, allThings = {} ):
        self.coordinates = (0, 0)
        self.greeting = ""
        self.direction = {}
        for side in allDirections:
            self.direction[side] = None
        self.allThings = allThings
        self.allBeasts = allBeasts
        self.possibleThings = []
        self.possibleBeasts = []
        self.thingsInRoom = [] # Оставленные вещи
        self.beastsInRoom = [] # Оставленные существа
        self.firstEnter = True


    def add_thing_into_room(self, thing):
        self.possibleThings.append( thing )

    def get_chose(self, chose):
        print("Function get_chose (",chose, ")")

    def read_from_file(self, fileStream):
        for line  in fileStream:
            try:
                words = utils.split_by_words(line)
            except ConfFileError as e:
                msg = "Ошибка при чтении описания комнаты в строке '" + line + \
                        "': " + e.what()
                raise ConfFileError(msg)

            if not words:
                continue
            if  words[0] == "#Coordinates": 
                self.coordinates = (int(words[1]), int(words[2]))
            elif words[0] == "#Wall":
                self.set_walls(words[1])
            elif words[0] == "#Thing":
                self.check_thing (words[1])
                self.possibleThings.append( PossibleThing( self.allThings[words[1]], probability = int(words[2])) )
            elif words[0] == "#Beast":
                self.check_beast(words[1])
                self.possibleBeasts.append( PossibleBeast( self.allBeasts[words[1]], probability = int(words[2])) )
            elif words[0] == "#Greeting":
                self.greeting = utils.read_until_empty_line( line[len(words[0]):], fileStream  )
            elif words[0] == "#EndRoom":
                return


    def set_walls(self, walls: str):
        if 'l' in walls:
            self.direction["left"] = Wall()
        if 'r' in walls:
            self.direction["right"] = Wall()
        if 'f' in walls:
            self.direction["front"] = Wall()
        if 'b' in walls:
            self.direction["back"] = Wall()


    def activate(self):
        print (self.greeting)

        for curBeast in self.possibleBeasts:
            if random()*100. < curBeast.appearanceProb:
                self.beastsInRoom.append(curBeast.beast)
        
        for curThing in self.possibleThings:
            if random()*100. < curThing.appearanceProb:
                self.thingsInRoom.append(curThing.thing)


    def check_thing(self, thingName):
        if thingName not in self.allThings.keys():
            msg  = "Ошибка. Нет конфигурации для вещи '" + thingName + "' " \
                    +  "в комнате " + str(self.coordinates)
            raise ConfFileError(msg)


    def check_beast(self, beastName):
        if beastName not in self.allBeasts.keys():
            msg  = "Ошибка. Нет конфигурации для вещи '" + beastName + "' " \
                    +  "в комнате " + str(self.coordinates)
            raise ConfFileError(msg)

    



