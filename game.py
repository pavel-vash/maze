#!/usr/bin/python3

from hero import Beast, Character
from thing import Thing
from maze import Maze

me = Character("Герой")
enemy = Beast("Враг")


maze = Maze()
maze.read_from_file ("maze_description.txt")

x = 0
y = 0



while True :

    maze.move_to_room( (x, y) )
    curRoom = maze.rooms[x, y]

    if ( len(curRoom.thingsInRoom) > 0 ):
        print("В комнате находятся:")
        for thing in curRoom.thingsInRoom:
            print(thing.name)

    if ( len(curRoom.beastsInRoom) > 0 ):
        print("А еще вылезли существа:\n")
        for beast in curRoom.beastsInRoom:
            print(beast.name)

    chose = input ("Ваш выбор:")

    curRoom.get_chose(chose)

    me.attacked_by (enemy)
    if not me.alive :
        print(me.name, "is dead")
        break

    print("My health=",me.health)

#    enemy.attacked_by(me)
    me.attack(enemy)
    if not enemy.alive:
        print(enemy.name, "is dead")
        break

    print(enemy.name,"'s health=",enemy.health)
