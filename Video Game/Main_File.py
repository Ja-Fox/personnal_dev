import time
import random
from Archmage_Class import Archmage
import Combat_Sequence
import Action_Choice
import Loot_Items
import Loot_Generator
import Use_Potion
import Monster_Location_Generator
from Monster_class import Boss_Monster
import Quest_Introduction
import Master_Map
import Character_Creation
import Use_Potion


if __name__ == '__main__':

    
## Scripted character for testing ##
    player_name = "Jason"
    player_health = 40    
    attributes = {}
    attributes['Strength'] = 20
    attributes['Constitution'] = 20
    attributes['Dexterity'] = 20
    attributes['Intelligence'] = 20
    attributes['Wisdom'] = 20
    attributes['Charisma'] = 20
    attributes['Luck'] = 20
    player_character = Archmage(player_name, attributes)
    print('\n')


 ## Character creation walkthrough, item generation, place the player on the map ##
    # player_character = Character_Creation.game_setup_and_intro()
    # player_health = player_character.starting_player_health()
    # print('\n')
    # player_name = player_character.player_name
    player_location = Character_Creation.player_starting_location()
    print(f'You mark your map with an X at your starting location of {player_location}')
    potion_inventory = []
    item_inventory = []
    potion_inventory , item_inventory = Character_Creation.character_inventory(potion_inventory,item_inventory,item_to_add='Health Potion')
    # player_items = ['Health Potion']


## Creates a boss monster and places it on the map ##
    # boss_location = {f'x':,'y':6}
    boss_instance = Boss_Monster()
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
    
## Game start ##
    while player_health > 0 and player_location != boss_location:
        
        action = input("""What is you action? Type 'help' for options. """).lower()

        if action == 'help':
            print("""
help     See options.             
hp       Check your current health. 
items    Check items in your inventory
magic    Check your magic ability descriptions.                     
map      Check the map.
melee    Check your melee ability descriptions.              
move     Move in a direction.
poiton   Heal yourself.
quit     End the game.                          
special  Check you weapon special ability description.              
""")
            time.sleep(2)
            print('\n')
            continue

## Quitting will end the game ##
        if action == 'quit':
            ending = f"Goodbye,{player_name}. Averfell will miss you."
            for character in ending:
                if character == ' ':
                    time.sleep(.3)
                print (character,end='',flush=True)
                time.sleep(.3)
            break

## This asks the player which way to move and updates the player's coordiantes ##
        if action == 'move':
            direction = Action_Choice.movement_choice()
            print (f"You walk {direction}...")
            player_location = Action_Choice.movement_execution(direction,player_location)
            

## Checks if player should fight the boss first ##
            if player_location == boss_location:
                player_health, potion_inventory, item_inventory = Combat_Sequence.boss_combat(player_health,player_character,potion_inventory,item_inventory,boss,boss_health)
                if player_health > 0:
                    ending = f"""You have slain the {boss}! The land feels the grip of terror lift as you emerge victorious from the beast's lair. 
Congratulations, {player_name}. Your name will become a part of local history. Perhaps even a local legend. Rest easy."""
                    for character in ending:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    time.sleep(3)
                    break
                
                elif player_health <= 0:
                    ending = f"""You were bested by the {boss}. The town lost another hero today...and the people remain under the grip of fear. """
                    for character in ending:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    time.sleep(3)    
                    break
            
## Then checks if player should fight a monster ##
            elif player_location in list_of_fights:
                player_health, potion_inventory, item_inventory = Combat_Sequence.easy_combat(player_health,player_character,potion_inventory, item_inventory)
                while player_location in list_of_fights:
                    list_of_fights.remove(player_location)
                time.sleep(2)

## If Player wins combat:
#### Loot Generator Chance --> Potion ##
                if (random.randint(1,10) % 2 == 0):
                    found_potion = Loot_Generator.potion_generator()
                    potion_text = "You found a potion!"
                    for character in potion_text:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    print('\n')
                    potion_inventory.append(found_potion)
                else:
                    continue

#### Loot Generator Chance --> Weapon ##
#### Equip Weapon Option ##
                if (random.randint(1,10) % 2 == 0):
                    weapon_text = "You found a weapon!"
                    for character in weapon_text:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    print('\n')
                    found_weapon = Loot_Generator.dependent_weapon_gen(player_character)
                    pick_it_up_text = "Do you want to equip it?"
                    for character in pick_it_up_text:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    answer = input().lower()
                    if answer == 'yes':
                        player_character.weapon = found_weapon
                    if answer == 'no':
                        continue
                else:
                    continue

## If there is no combat ##
            else:
                no_encounter = f"The path remains clear...for now. Continue moving."
                for character in no_encounter:
                    if character == ' ':
                        time.sleep(.03)
                    print (character,end='',flush=True)
                    time.sleep(.03)
                print('\n')

## Lists magic abilities and descriptions ##
        if action == 'magic':
            player_character.ability_descriptions()
            time.sleep(2)
            print('\n')

## Lists melee abilities and descriptions ##
        if action == 'melee':
            print(player_character.weapon.abilities[0],player_character.weapon.abilities[1],player_character.weapon.abilities[2])
            time.sleep(2)
            print('\n')

## Lists weapon special ability and description ##
        if action == 'special':
            print(f"""
{player_character.weapon.special_ability}:
{player_character.weapon.special_ability_description}
""")
            time.sleep(2)
            print('\n')

## Lists item inventory ##
        if action == 'items':
            print (f'Your potions: {potion_inventory}')
            print (f'Your items:{item_inventory}')
            time.sleep(1)
            print('\n')

## Reports Hit Points ##
        if action == 'hp':
            health_check = f"You currently have {player_health} hit points."
            for character in health_check:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            time.sleep(1)
            print('\n')

## Prompts Potion Use interaction ##
        if action == 'potion':
            if len(potion_inventory) > 0 :
                Loot_Items.list_potions_in_inventory()
                question = "Which potion would you like to use? Type only the first word. "
                for character in question:
                    if character == ' ':
                        time.sleep(.05)
                    print (character,end='',flush=True)
                    time.sleep(.05)
                potion_to_use = input().title()
                if potion_to_use == 'Minor':
                    player_health = Use_Potion.use_minor_health_potion(player_health)
                elif potion_to_use == 'Health':
                    player_health = Use_Potion.use_health_potion(player_health)
                elif potion_to_use == 'Greater':
                    player_health = Use_Potion.use_greater_health_potion(player_health)
                elif potion_to_use == 'Life':
                    player_health = Use_Potion.use_life_potion(player_health)
                potion_inventory.remove(potion_to_use)
                output = f"You healed to {player_health} HP."
                for character in output:
                    if character == ' ':
                        time.sleep(.05)
                    print (character,end='',flush=True)
                    time.sleep(.05)

            else:
                output = "You have no more potions."
                for character in output:
                    if character == ' ':
                        time.sleep(.05)
                    print (character,end='',flush=True)
                    time.sleep(.05)

## Displays the Map for the player ##
        if action == 'map':
            location = f"Your coordiantes are {player_location}"
            for character in location:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            Master_Map.map_check()
    
    print('\n')
    
    print("I hope you enjoyed this little game I made!")
    time.sleep(5)