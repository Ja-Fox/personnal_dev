import time
import Paladin_Class
import Lionheart_Class
import Ritualist_Class
import Archmage_Class
import Assassin_Class
import SpellShot_Class


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
        player_character = Paladin_Class.Paladin(player_name,attributes)
        
    elif character_class == 'Lionheart':
        player_character = Lionheart_Class.Lionheart(player_name,attributes)

    elif character_class == 'Ritualist':
        player_character = Ritualist_Class.Ritualist(player_name,attributes)

    elif character_class == 'Archmage':
        player_character = Archmage_Class.Archmage(player_name,attributes)

    elif character_class == 'Assassin':
        player_character = Assassin_Class.Assassin(player_name,attributes)

    elif character_class == 'Spellshot':
        player_character = SpellShot_Class.Spell_Shot(player_name,attributes) 

    return player_character