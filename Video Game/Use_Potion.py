import Loot_Items



def use_minor_health_potion(player_health):
    player_health += Loot_Items.Minor_Health_Potion
    return player_health

def use_health_potion(player_health):
    player_health += Loot_Items.Health_Potion
    return player_health

def use_greater_health_potion(player_health):
    player_health += Loot_Items.Greater_Health_Potion 
    return player_health

def use_life_potion(player_health):
    player_health += Loot_Items.Life_Potion
    return player_health
