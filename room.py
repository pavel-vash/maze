from exceptions import *
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





class Room:
    def __init__(self, coordinates = (0, 0) ):
        self.direction = {}
        for side in allDirections:
            self.direction[side] = None
        self.things = []
        self.beasts = []
        self.greeting = ""
        self.variants = dict()
        self.coordinates = coordinates
        self.firstEnter = True


    def add_thing_into_room(self, things):
        self.things = things

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
                self.things.append( [ words[1], int(words[2])] )
            elif words[0] == "#Beast":
                self.beasts.append( [ words[1], int(words[2])] )
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






        




    



