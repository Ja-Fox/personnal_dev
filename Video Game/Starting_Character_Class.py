import time

def starting_character_class():
    print("Welcome Adventurer...")
    time.sleep(2)
    print("You must now create your character.")
    time.sleep(2)
    print("""
Choose your class:
Warrior
Mage
Rogue 
          
Type HELP to read more about each class.""")
    while True:
        character_class = input("Make your choice: ").lower()

        if character_class == 'help':
            print("""
    Warrior:
    A front-line, tank-like class. The warrior class can take heavy damage and keep fighting.
    The warrior's primary attributes are Strength, Constitution, and Dexterity.
                
    Subclasses: Lionheart, Paladin
                
                    
    Mage:
    A spellcaster class. The mage class can learn a range of  deadly spells, but
    cannot take much damage. The mage's primary attributes are Intelligence,
    Wisdom, and Luck.
                
    Subclasses: Archmage, Ritualist
                            
                
    Rouge:
    A mid-line class, able to specialize in either ranged or melee comabt. 
    The rouge's primary attributes are Dexterity, Charisma, and Wisdom.

    Subclasses: Assassin, Spell Shot""")
            continue

        if character_class == 'warrior':
            print(f"You have chosen to be a {character_class}.")
            time.sleep(1)

            print("Choose your subclass:")
            print("""
    Battleborn - XXX
    Paladin - gain access to holy magic and choose a Path to follow.
    """)
            character_subclass = input().title()
            print(f"You have chosen to be a {character_subclass}")
            return character_class

        if character_class == 'rogue':
            print(f"You have chosen to be a {character_class}.")
            time.sleep(1)

            print("Choose your subclass:")
            print("""
    Assassin - XXX
    Spell Shot - XXX
    """)
            character_subclass = input().title()
            print(f"You have chosen to be a {character_subclass}")
            return character_class

        if character_class == 'mage':
            print(f"You have chosen to be a {character_class}.")
            time.sleep(1)

            print("Choose your subclass:")
            print("""
    Archmage - XXX
    Ritualist - XXX
    """)
            character_subclass = input().title()
            print(f"You have chosen to be a {character_subclass}")
            return character_subclass
