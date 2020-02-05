#!/usr/bin/python3
import sys

from hero import Beast, Character
from thing import Thing
from exceptions import ConfFileError
import utils
from room import *



class Maze:
    def __init__(self):
        self.beasts = {}
        self.things = {}
        self.rooms  = {}
    

    def read_from_file(self, fileName):
        pass
        
    def move_to_room(self, coords):
        curRoom = self.rooms[coords]
        if curRoom.firstEnter :
            curRoom.activate()
            curRoom.firstEnter = False
        else:
            curRoom.reactivate()




    def read_from_file(self, fileName):
        f = open(fileName)
        for line in f:
            words = utils.split_by_words(line)
            if not words :
                continue
            if words[0] == "#include":
                self.read_from_file(words[1])
            elif words[0] == "#Beast":
                newBeast = Beast("")
                newBeast.read_from_file(f)
                self.beasts[newBeast.name] = newBeast
            elif words[0] == "#Thing":
                newThing = Thing("")
                newThing.read_from_file(f)
                self.things[newThing.name] = newThing
            elif words[0] == "#Room":
                newRoom = Room(self.beasts, self.things)
                newRoom.read_from_file(f)
                self.check_room_correctness(newRoom)
                self.rooms[newRoom.coordinates] = newRoom

             

    def check_room_correctness(self, room):
        try:
            if  room.coordinates in self.rooms.keys():
                msg = "Ошибка: комната " + str(room.coordinates) + \
                        " задана дважды"
                raise ConfFileError(msg)

            self.check_walls_in_room(room)
#            self.check_things_in_room(room)
#            self.check_beasts_in_room(room)
        except ConfFileError as e:
            print("Ошибка в конфигурации комнаты (",
                  room.coordinates, "):\n", e.what() )
            sys.exit()


    def check_walls_in_room(self, curRoom: Room):

        for side in allDirections:
            neigh= self.neighbour(curRoom, side)
            if neigh in self.rooms.keys():
                if curRoom.direction[side] != self.rooms[neigh].direction[oppositeDirections[side]]:
                    msg = "Ошибка в конфигурации. Комната #Room ", \
                          curRoom.coordinates, " конфликтует с комнатой #Room", \
                          self.rooms[neigh].coordinates 
                    raise ConfFileError(msg)
                

        
    def room_neighbours(self, room: Room):
        
        allNeighbours = self.all_neigbours(room)
        for neigh in allNeighbours:
            if  neigh in self.rooms.keys():
                neighbours.append(neigh)

        return neighbours

    def all_neigbours(self, room):
        allNeighbours = []
        allNeighbours.append(self.neighbour(room, "left"))
        allNeighbours.append(self.neighbour(room, "right"))
        allNeighbours.append(self.neighbour(room, "back"))
        allNeighbours.append(self.neighbour(room, "front"))
        return allNeighbours




    def neighbour(self, room: Room, side : str ):
        x,y = room.coordinates

        if side == "left": 
            return ( x-1, y )
        elif side == "right":
            return ( x+1, y )
        elif side == "back":
            return ( x, y-1 )
        elif side == "front":
            return ( x, y+1 )



