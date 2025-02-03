import Loot_Items
import Main_File


def use_minor_health_potion(potion,health):
    health += potion.heal
    return health

def use_health_potion(potion,health):
    health += potion.heal
    return health

def use_greater_health_potion(potion,health):
    health += potion.heal 
    return health

def use_life_potion(potion,health):
    health += potion.heal
    return health
