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

actionVariants = {
    "t": "Взять вещь",                      \
    "h": "Ударить врага",                   \
    "a": "Пойти влево",                     \
    "s": "Пойти назад",                     \
    "d": "Пойти вправо",                    \
    "w": "Пойти вперед",                    \
    "i": "Заглянуть в мешок",               \
    "m": "Открыть карту",                   \
    "v": "Посмотреть характеристики вещи или врага", \
}


while True :

    maze.move_to_room( (x, y) )
    curRoom = maze.rooms[x, y]

    if ( len(curRoom.thingsInRoom) > 0 ):
        print("В комнате находятся:")
        for thing in curRoom.thingsInRoom:
            print(thing.name)

    if ( len(curRoom.beastsInRoom) > 0 ):
        print("А еще вылезли существа:")
        for beast in curRoom.beastsInRoom:
            print(beast.name)

    while True:
        ask = ""
        for key in actionVariants:
            ask += key + " : " + actionVariants[key] + "\n"

        choice = input (ask)

        if choice == "t":
            take_thing(curRoom.thingsInRoom)
        elif choice == "h":
            hit_enemy(curRoom.beastsInRoom)
        elif choice == "i":
            look_at_invenories()
        elif choice == "m":
            show_map()
        elif choice == "v":
            show_parameters(curRoom.thingsInRoom, curRoom.beastsInRoom)
        elif choice == "a":
            enemy_action(curRoom.beastsInRoom)
            x = x-1
            continue
        elif choice == "s":
            enemy_action(curRoom.beastsInRoom)
            y = y-1
            continue
        elif choice == "d":
            enemy_action(curRoom.beastsInRoom)
            x = x+1
            continue
        elif choice == "w":
            enemy_action(curRoom.beastsInRoom)
            y = y+1
            continue
        else:
            print("Неизвестное действие")
            pass




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
