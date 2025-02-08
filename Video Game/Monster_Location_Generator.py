import random


def number_of_monsters_to_fight():
    number_to_fight = random.randint(25,35)
    return number_to_fight


def monster_coordiantes_generator():
    xlst = [-3,-2,-1,0,1,2,3]
    ylst = [-4,-3,-2,-1,0,1,2,3,4,5,6]
    x = random.choice(xlst)
    y = random.choice(ylst)
    monster_location = {'x':x,'y':y}
    return monster_location


def monster_location_list_generator(number_of_monsters_fight):
    list_of_monster_coordinates = []
    for i in range(1,number_of_monsters_fight):
        monster_location = monster_coordiantes_generator()
        list_of_monster_coordinates.append(monster_location)
    return list_of_monster_coordinates


