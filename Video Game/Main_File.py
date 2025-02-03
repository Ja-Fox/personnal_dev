import time
import random
from Ritualist_Class import Ritualist
from Archmage_Class import Archmage
from Paladin_Class import Paladin
from Lionheart_Class import Lionheart
from Assassin_Class import Assassin
from SpellShot_Class import Spell_Shot
# from Monster_class import Monster
# from Character_Name import character_name
# from Starting_Character_Class import starting_character_class
# from Starting_Character_Attributes import starting_character_attributes
import Combat_Sequence
import Weapon_Classes
import Action_Choice
import Loot_Items
import Loot_Generator
import Use_Potion
import Monster_Location_Generator
from Monster_class import Boss_Monster
import Quest_Introduction
import Master_Map

def starting_character_class():
    text= "Welcome Adventurer..."
    for character in text:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)
    time.sleep(1)
    print('\n')
    text2 = "You must now create your character."
    for character in text2:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)
    print('\n')
    time.sleep(1)
    print("""
Choose your class:
Warrior
Mage
Rogue 
          
Type HELP to read more about each class.""")
    while True:
        char_class = input("Make your choice: ").lower()

        if char_class == 'help':
            descriptions= f"""
    Warrior:
    A front-line, tank-like class. The warrior class can take heavy damage and keep fighting.
    The warrior's primary attributes are Strength, Constitution, and Dexterity.

    Subclasses: Lionheart, Paladin


    Mage:
    A spellcaster class. The mage class can learn a range of deadly spells, but
    cannot take much damage. The mage's primary attributes are Intelligence,
    Wisdom, and Luck.

    Subclasses: Archmage, Ritualist


    Rogue:
    A mid-line class, able to specialize in either ranged or melee combat. 
    The rouge's primary attributes are Dexterity, Wisdom, and Charisma.

    Subclasses: Assassin, Spellshot"""
            for character in descriptions:
                if character == ' ':
                    time.sleep(.04)
                print (character,end='',flush=True)
                time.sleep(.04)
            print('\n')    
            continue

        if char_class == 'warrior':
            text = f"You have chosen to be a {char_class}.\n"
            for character in text:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            time.sleep(1)
            print('\n')
            print("Choose your subclass:")
            text3 = f"""
    Lionheart - A warrior who finds focus in chaos
    Paladin - A holy warrior, blessed by the Gods to fight evil"""
            for character in text3:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            print('\n')
            character_class = input().title()
            print('\n')
            choice = f"You have chosen to be a {character_class}"
            for character in choice:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            print('\n')
            return character_class

        if char_class == 'rogue':
            text = f"You have chosen to be a {char_class}.\n"
            for character in text:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            time.sleep(1)
            print("Choose your subclass:")
            text3 = f"""
    Assassin - A master of lethality and surpirse, preferring to fight up-close
    Spellshot - A honed marksman with magic capabilities, keeping enemies at bay with range"""
            for character in text3:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            print('\n')
            character_class = input().title()
            choice = f"You have chosen to be a {character_class}"
            for character in choice:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            return character_class

        if char_class == 'mage':
            text = f"You have chosen to be a {char_class}.\n"
            for character in text:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            time.sleep(1)
            print("Choose your subclass:")
            text3 = f"""
    Archmage - The pinical of magical power, capable of harnessing the elements
    Ritualist - A conduit for the Afterlife, utilizing the Beyond to strike at the living"""
            for character in text3:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            print('\n')
            character_class = input().title()
            choice = f"You have chosen to be a {character_class}"
            for character in choice:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            return character_class

def starting_character_attributes():
    point_pool = 20
    attributes= {}

    strength = 8
    constitution = 8
    dexterity = 8
    intelligence = 8
    wisdom = 8
    charisma = 8
    luck = 8
    print(f"""You have {point_pool} points to distribute:
Strength        {strength}
Constitution    {constitution}
Dexterity       {dexterity}
Intelligence    {intelligence}
Wisdom          {wisdom}
Charisma        {charisma}
Luck            {luck} 

Use STR | CON | DEX | INT | WIS | CHA | LUK to identify the
the attribute you wish to alter.
""")
    while point_pool > 0:
        answer = input("""Which attribute do you want to increase? Type 'help' to read each attribute's impact.""").lower()

        if answer == 'help':
            explanation = f""" 
Strength        Increases how hard your melee attacks hit.
                For Warriors: Your abilities and damage thresholds are primarily based off of this trait.

Constitution    Increases your base health (potions can raise your HP higher than your base starting level).

Dexterity       Increases your chances of escape.  
                For Rogues: Your abilities and damage thresholds are primarily based off of this trait.

Intelligence    For Mages: Your abilities and damage thresholds are heavily based off of this trait.

Wisdom          For Rogues: Your magic-based abilities are influenced by this trait.
                For Mages: You abilities are influenced by this trait to a lesser degree.

Charisma        --NOT USED IN THIS VERSION--

Luck            --NOT USED IN THIS VERSION--
"""
            for character in explanation:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            print('\n')

        elif answer == 'str':
            amount = int(input("How many points do you want to allocate? "))
            strength += amount
            point_pool -= amount
            if amount > 0:
                print(f"Strength increased to {strength}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Strength decreased to {strength}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

        elif answer == 'con':
            amount = int(input("How many points do you want to allocate? "))
            constitution += amount
            point_pool -= amount
            if amount > 0:
                print(f"Constitution increased to {constitution}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Constitution decreased to {constitution}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

        elif answer == 'dex':
            amount = int(input("How many points do you want to allocate? "))
            dexterity += amount
            point_pool -= amount
            if amount > 0:
                print(f"Dexterity increased to {dexterity}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Dexterity decreased to {dexterity}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

        elif answer == 'int':
            amount = int(input("How many points do you want to allocate? "))
            intelligence += amount
            point_pool -= amount
            if amount > 0:
                print(f"Intelligence increased to {intelligence}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Intelligence decreased to {intelligence}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

        elif answer == 'wis':
            amount = int(input("How many points do you want to allocate? "))
            wisdom += amount
            point_pool -= amount
            if amount > 0:
                print(f"Wisdom increased to {wisdom}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Wisdom decreased to {wisdom}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

        elif answer == 'cha':
            amount = int(input("How many points do you want to allocate? "))
            charisma += amount
            point_pool -= amount
            if amount > 0:
                print(f"Charisma increased to {charisma}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Charisma decreased to {charisma}")
                print(f"You have {point_pool} points left to use.")
                print('\n')
            
        elif answer == 'luk':
            amount = int(input("How many points do you want to allocate? "))
            luck += amount
            point_pool -= amount
            if amount > 0:
                print(f"Luck increased to {luck}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

            elif amount < 0:
                print(f"Luck decreased to {luck}")
                print(f"You have {point_pool} points left to use.")
                print('\n')

        else:
            print("Input was not an atribute.")
            print('\n')
    time.sleep(1.5)
    print(f""" Your final stats:
Strength        {strength}
Constitution    {constitution}
Dexterity       {dexterity}
Intelligence    {intelligence}
Wisdom          {wisdom}
Charisma        {charisma}
Luck            {luck}
""")
    attributes['Strength'] = strength
    attributes['Constitution'] = constitution
    attributes['Dexterity'] = dexterity
    attributes['Intelligence'] = intelligence
    attributes['Wisdom'] = wisdom
    attributes['Charisma'] = charisma
    attributes['Luck'] = luck

    return attributes
    
def character_name():
    text = "Now, choose a name.\n"
    for character in text:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)
    player_name = input().title()
    print('\n')
    time.sleep(1)

    text2 = f"Welcome to your adventure, {player_name}."
    for character in text2:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)
    time.sleep(1)
    print('\n')
    return player_name

def game_setup_and_intro():
    character_class = starting_character_class()
    attributes = starting_character_attributes()
    player_name = character_name()

    if character_class == 'Paladin':
        player_character = Paladin(player_name,attributes)
        
    elif character_class == 'Lionheart':
        player_character = Lionheart(player_name,attributes)

    elif character_class == 'Ritualist':
        player_character = Ritualist(player_name,attributes)

    elif character_class == 'Archmage':
        player_character = Archmage(player_name,attributes)

    elif character_class == 'Assassin':
        player_character = Assassin(player_name,attributes)

    elif character_class == 'Spellshot':
        player_character = Spell_Shot(player_name,attributes) 

    return player_character
    # health = player_character.starting_player_health()
    # print(f"""You begin you your journey with {health} hit points.""")

if __name__ == '__main__':
    
    ## Scripted character for testing ##
    # player_name = "Jason"    
    # attributes = {}
    # attributes['Strength'] = 20
    # attributes['Constitution'] = 20
    # attributes['Dexterity'] = 20
    # attributes['Intelligence'] = 20
    # attributes['Wisdom'] = 20
    # attributes['Charisma'] = 20
    # attributes['Luck'] = 20
    # player_character = Archmage(player_name, attributes)
    print('\n')

    ## Character creation walkthrough, item generation, place the player on the map ##
    player_character = game_setup_and_intro()
    player_health = player_character.starting_player_health()
    print('\n')
    player_name = player_character.player_name
    player_location = {'x':3,'y':-4}
    player_items = ["Health Potion"]

    ## Creates a boss monster and places it on the map ##
    boss_location = {'x':-4,'y':6}
    boss_instance = Boss_Monster()
    boss = boss_instance.get_boss_monster_encounter()
    boss_health = boss_instance.get_boss_monster_health()   
    
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
    starting_location = Quest_Introduction.Starting_Village()
    print('\n')
    time.sleep(5)
    Master_Map.master_map(starting_location)
    
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

        if action == 'quit':
            ending = f"Goodbye,{player_name}. Averfell will miss you."
            for character in ending:
                if character == ' ':
                    time.sleep(.3)
                print (character,end='',flush=True)
                time.sleep(.3)
            break

        if action == 'move':
            ## This asks the player which way to move and updates the player's coordiantes ##
            # direction, distance = Action_Choice.movement_choice()
            direction = Action_Choice.movement_choice()
            print (f"You walk {direction}...")
            # player_location = Action_Choice.movement_execution(direction,distance,player_location)
            player_location = Action_Choice.movement_execution(direction,player_location)
            
            ## Checks if player should fight the boss ##
            if player_location == boss_location:
                player_health, player_items = Combat_Sequence.boss_combat(player_health,player_character,player_items,boss,boss_health)
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
            
            ## Checks if player should fight a monster ##
            elif player_location in list_of_fights:
                player_health, player_items = Combat_Sequence.easy_combat(player_health,player_character,player_items)
                while player_location in list_of_fights:
                    list_of_fights.remove(player_location)
                time.sleep(2)
                found_potion = Loot_Generator.potion_generator()
                potion_text = "You found a potion!"
                for character in potion_text:
                    if character == ' ':
                        time.sleep(.05)
                    print (character,end='',flush=True)
                    time.sleep(.05)
                print('\n')
                player_items.append(found_potion)
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
                no_encounter = f"The path remains clear...for now. Continue moving."
                for character in no_encounter:
                    if character == ' ':
                        time.sleep(.03)
                    print (character,end='',flush=True)
                    time.sleep(.03)
                print('\n')

        if action == 'magic':
            player_character.ability_descriptions()
            time.sleep(2)
            print('\n')

        if action == 'melee':
            print(player_character.weapon.abilities[0],player_character.weapon.abilities[1],player_character.weapon.abilities[2])
            time.sleep(2)
            print('\n')

        if action == 'special':
            print(f"""
{player_character.weapon.special_ability}:
{player_character.weapon.special_ability_description}
""")
            time.sleep(2)
            print('\n')

        if action == 'items':
            print (player_items)
            time.sleep(1)
            print('\n')

        if action == 'hp':
            health_check = f"You currently have {player_health} hit points."
            for character in health_check:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
            time.sleep(1)
            print('\n')

        if action == 'potion':
            if len(player_items) > 0 :
                for each_potion in player_items:
                    print (each_potion)
                question = "Which potion would you like to use? "
                for character in question:
                    if character == ' ':
                        time.sleep(.05)
                    print (character,end='',flush=True)
                    time.sleep(.05)
                potion_to_use = input().title()

                if potion_to_use == 'Minor Health Potion':
                    player_health = Use_Potion.use_minor_health_potion(Loot_Items.Minor_Health_Potion(),player_health)
                    output = f"You healed to {player_health} HP."
                    for character in output:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    player_items.remove(potion_to_use)

                if potion_to_use == 'Health Potion':
                    player_health = Use_Potion.use_health_potion(Loot_Items.Health_Potion(),player_health)
                    output = f"You healed to {player_health} HP."
                    for character in output:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    player_items.remove(potion_to_use)

                if potion_to_use == 'Greater Health Potion':
                    player_health = Use_Potion.use_greater_health_potion(Loot_Items.Greater_Health_Potion(),player_health)
                    output = f"You healed to {player_health} HP."
                    for character in output:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    player_items.remove(potion_to_use)

                if potion_to_use == 'Life Potion':
                    player_health = Use_Potion.use_life_potion(Loot_Items.Life_Potion(),player_health)
                    output = f"You healed to {player_health} HP."
                    for character in output:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)
                    player_items.remove(potion_to_use)

            else:
                output = "You have no more potions."
                for character in output:
                        if character == ' ':
                            time.sleep(.05)
                        print (character,end='',flush=True)
                        time.sleep(.05)

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