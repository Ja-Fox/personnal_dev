import Loot_Items


def use_minor_health_potion(player_health):
    heal_amount = Loot_Items.Minor_Health_Potion()
    player_health += heal_amount.heal
    return player_health

def use_health_potion(player_health):
    heal_amount = Loot_Items.Health_Potion()
    player_health += heal_amount.heal
    return player_health

def use_greater_health_potion(player_health):
    heal_amount = Loot_Items.Greater_Health_Potion()
    player_health += heal_amount.heal
    return player_health

def use_life_potion(player_health):
    heal_amount = Loot_Items.Life_Potion()
    player_health += heal_amount.heal
    return player_health
