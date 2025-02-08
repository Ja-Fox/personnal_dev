import time
import Monster_Location_Generator
import Monster_class
import Quest_Introduction
import Master_Map
import Character_Creation
import Game_Loop


if __name__ == '__main__':

## Character creation walkthrough, item generation, place the player on the map ##
    player_character = Character_Creation.game_setup_and_intro()
    player_health = player_character.starting_player_health()
    print('\n')
    player_name = player_character.player_name
    player_location = Character_Creation.player_starting_location()
    print(f'You start at of {player_location}')
    potion_inventory = ['Health Potion','Minor Health Potion']
    item_inventory = []
    potion_inventory , item_inventory = Character_Creation.character_inventory(potion_inventory,item_inventory,item_to_add='Health Potion')


## Creates a boss monster and places it on the map ##
    # boss_location = {f'x':-3,'y':6}
    boss_instance = Monster_class.Boss_Monster()
    boss = boss_instance.get_boss_monster_encounter()
    boss_health = boss_instance.get_boss_monster_health()
    boss_location = boss_instance.get_boss_monster_location()
    

## Generates random number of encouters and places them on the map ## 
    number_of_monsters_to_fight = Monster_Location_Generator.number_of_monsters_to_fight()
    list_of_fights = Monster_Location_Generator.monster_location_list_generator(number_of_monsters_to_fight)

## Interlude ##
    elipse = ".........."
    for character in elipse:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.25)
    print('\n')
    for character in elipse:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.25)
    print('\n')
    for character in elipse:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.25)
    print('\n')

## Quest Generation and Delivery ##
    Quest_Introduction.Quest_Text(boss,player_name)
    print('\n')
    time.sleep(2)
    starting_village = Quest_Introduction.Starting_Village()
    print('\n')
    time.sleep(5)
    Master_Map.master_map(player_location)
    
## Game loop start ##

(player_name, player_character, player_health, player_location, potion_inventory, item_inventory,
boss, boss_health, boss_location,
number_of_monsters_to_fight, list_of_fights,
starting_village) = Game_Loop.game_loop(player_name, player_character, player_health, player_location, potion_inventory, item_inventory,
        boss, boss_health, boss_location,
        number_of_monsters_to_fight, list_of_fights,
        starting_village)

print("\nI hope you enjoyed this little game I made!")
time.sleep(5)