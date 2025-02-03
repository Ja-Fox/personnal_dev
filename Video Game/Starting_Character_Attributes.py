import time
def starting_character_attributes():
    point_pool = 18
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
        answer = input("""Which attribute do you want to increase?""").lower()

        if answer == 'str':
            amount = int(input("How many points do you want to allocate? "))
            strength += amount
            point_pool -= amount
            if amount > 0:
                print(f"Strength increased to {strength}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Strength decreased to {strength}")
                print(f"You have {point_pool} points left to use.", end='\n')

        elif answer == 'con':
            amount = int(input("How many points do you want to allocate? "))
            constitution += amount
            point_pool -= amount
            if amount > 0:
                print(f"Constitution increased to {constitution}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Constitution decreased to {constitution}")
                print(f"You have {point_pool} points left to use.", end='\n')

        elif answer == 'dex':
            amount = int(input("How many points do you want to allocate? "))
            dexterity += amount
            point_pool -= amount
            if amount > 0:
                print(f"Dexterity increased to {dexterity}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Dexterity decreased to {dexterity}")
                print(f"You have {point_pool} points left to use.", end='\n')

        elif answer == 'int':
            amount = int(input("How many points do you want to allocate? "))
            intelligence += amount
            point_pool -= amount
            if amount > 0:
                print(f"Intelligence increased to {intelligence}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Intelligence decreased to {intelligence}")
                print(f"You have {point_pool} points left to use.", end='\n')

        elif answer == 'wis':
            amount = int(input("How many points do you want to allocate? "))
            wisdom += amount
            point_pool -= amount
            if amount > 0:
                print(f"Wisdom increased to {wisdom}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Wisdom decreased to {wisdom}")
                print(f"You have {point_pool} points left to use.", end='\n')

        elif answer == 'cha':
            amount = int(input("How many points do you want to allocate? "))
            charisma += amount
            point_pool -= amount
            if amount > 0:
                print(f"Charisma increased to {charisma}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Charisma decreased to {charisma}")
                print(f"You have {point_pool} points left to use.", end='\n')
            
        elif answer == 'luk':
            amount = int(input("How many points do you want to allocate? "))
            luck += amount
            point_pool -= amount
            if amount > 0:
                print(f"Luck increased to {luck}")
                print(f"You have {point_pool} points left to use.", end='\n')
            elif amount < 0:
                print(f"Luck decreased to {luck}")
                print(f"You have {point_pool} points left to use.", end='\n')

        else:
            print("Input was not an atribute.")

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