import time
import random
# from Starting_Character_Class import starting_character_class
from Defense_Againse_Monster import defense_against_monster
from Monster_class import Monster
from Monster_class import Boss_Monster
import Weapon_Classes
import Loot_Items
import Use_Potion


def easy_flee_combat(player_character):
    flee_role = player_character.flee_attempt()
    if flee_role >= 13:
        return True
    else:
        return False

def easy_combat(player_health, player_character, potion_inventory, item_inventory):
    monster = Monster()
    encounter = monster.get_easy_monster_encounter()
    monster_health = monster.get_easy_monster_health()
    
    print(f"""A {encounter} appears!""")

    time.sleep(1)

    answer = input('Do you fight or flee? ').lower()

    if answer == 'flee':
        success = easy_flee_combat(player_character)
        if success is True:
            print ('You escape!')
            return player_health, potion_inventory, item_inventory
        else:
            pass
        answer = 'fight'
        # if flee_role >= 13:
        #     print("You escape!")
        #     return player_health,potion_inventory, item_inventory

        # else:
        #     print("Flee failed! Ready yourself for combat!")
        # answer == 'fight'
    #         while (player_health > 0) and (monster_health > 0):
            
    #             print("""Magic | Melee | Special | Use Potion""")
                
    #             combat_choice = input("You must make a decision: ").lower()

    #             if combat_choice == 'magic':
    #                 print("Your spell options are:")
    #                 options = ['A','B','C','D']
    #                 for options,each_spell in zip(options,player_character.spells):
    #                     print(f"""{options} - {each_spell}""")
    #                 print ("\nMake your choice: ")
                    
    #                 spell_choice = input().lower()

    #                 spell_hit = player_character.combat_magic_hit_modifier()
    #                 spell_dmg = player_character.combat_magic_dmg_modifier(spell_choice)

    #                 if spell_hit > 11:
    #                     print(f"You cast {spell_choice} and it connects! You deal {spell_dmg} damage!")
    #                     if monster_health <= spell_dmg:
    #                         monster_health = 0

    #                     elif monster_health > spell_dmg:
    #                         print(f"Your spell hits, but does not kill the monster!")
    #                         monster_health = monster_health - spell_dmg

    #                         time.sleep(1.5)

    #                         print("You must now ready yourself for a counter attack.")
                            
    #                         time.sleep(3)

    #                         player_health = defense_against_monster(player_character,potion_inventory, item_inventory)
    #                         print(f"""You have {player_health} HP left. """)
    #                         time.sleep(1)

    #                 else:
    #                     print(f"""You cast {spell_choice} but it misses!""")
    #                     print("Prepare to defend yourself!")
                        
    #                     time.sleep(2)

    #                     player_health = defense_against_monster(player_character,player_health)
    #                     print(f"You have {player_health} HP left.")
                    
    #             if combat_choice == 'melee':
    #                 print('Your options are:')
    #                 for each_ability in player_character.weapon.abilities:
    #                     print(each_ability, end ='  ')
    #                 print("\nMake your choice. ")

    #                 ability_choice = input().title()

    #                 ability_hit = player_character.combat_melee_hit_modifier()
    #                 ability_dmg = player_character.weapon.melee_dmg(ability_choice)
    #                 modifier = player_character.combat_melee_dmg_modifier(ability_choice)
    #                 ability_dmg += modifier

    #                 if ability_hit > 10:
    #                     print(f"{ability_choice} connects! You deal {ability_dmg}.")
    #                     if monster_health <= ability_dmg:
    #                         monster_health = 0
                        
    #                     elif monster_health > ability_dmg:
    #                         print("Your attack hits, but does not kill the enemy.")
    #                         monster_health = monster_health - ability_dmg

    #                         time.sleep(1.5)

    #                         print("Prepare for a counterattack!")

    #                         time.sleep(1.5)

    #                         player_health = defense_against_monster(player_character,player_health)
    #                         print(f" You have {player_health} HP left.")
    #                         time.sleep(1)
                        
    #                 else:
    #                     print(f"""{ability_choice} misses!""")
    #                     time.sleep(1)

    #                 print("Defend yourself!")
                    
    #                 time.sleep(2)

    #                 player_health = defense_against_monster(player_character,player_health)
    #                 print(f"You have {player_health} HP left.")

    #             if combat_choice == 'special':
    #                 try:
    #                     special_ability, special_ability_description = player_character.weapon.get_special_ability()
    #                     # special_ability_description = player_character.weapon.special_ability_description
    #                     print(f"""Your weapon's special ability is:
    # {special_ability} - {special_ability_description}""")
    #                     time.sleep(.5)

    #                     use_spec_answer = input("Do you want to use it? ").lower()
    #                     if use_spec_answer == 'no':
    #                         continue
    #                     elif use_spec_answer == 'yes':
    #                         print(f"You use {special_ability.split(' - ')[0]}.")
    #                         # print(f"You use {special_ability}")
    #                         player_health, dmg = player_character.weapon.special_ability_actions(player_character, player_health)
    #                         if monster_health <= dmg:
    #                             monster_health = 0
    #                             break
                            
    #                         else:
    #                             monster_health -= dmg

    #                         time.sleep(1)

    #                         print("Your enemy moves to attack!")

    #                         time.sleep(1)

    #                         player_health = defense_against_monster(player_character,player_health)
    #                         print(f" You have {player_health} HP left.")
    #                         time.sleep(1)
                        
    #                 except NotImplementedError:
    #                     print("Your weapon has no special ability!")
    #                     time.sleep(1)
                        
    #                 # defense_chance = random.randint (1,20)
    #                 # dmg_to_player = random.randint (1,10)
                    
    #                 # if defense_chance == 20:
    #                 #     dmg_to_player = 0
    #                 #     print (f"""You take {dmg_to_player} damage!
    #                 #         But don't rejoin too soon.
    #                 #         Prepare your next move.""")

    #                 # elif 9 < defense_chance < 20:
    #                 #     dmg_to_player = dmg_to_player // 2
    #                 #     player_health = player_health - dmg_to_player
    #                 #     print(f"""You ready yourself for impact.
    #                 #         You suffer {dmg_to_player} damage.""")
                        
    #                 #     if player_health <= 0:
    #                 #         print("You died.")
    #                 #         break

    #                 # if 2 <= defense_chance <= 9:
    #                 #     dmg_to_player = dmg_to_player - 2
    #                 #     player_health = player_health - dmg_to_player
    #                 #     print(f"""You take a brutal blow and suffer {dmg_to_player} damage.""")

    #                 #     if player_health <= 0:
    #                 #         print("You died.")
    #                 #         break

    #             if combat_choice == 'use potion':
    #                 if len(potion_inventory) > 0:
    #                     print (potion_inventory)
    #                     potion_to_use = input("Which potion would you like to use? Only type the first word. ").title()

    #                     if potion_to_use == 'Minor':
    #                         player_health = Use_Potion.use_minor_health_potion(player_health)
    #                     elif potion_to_use == 'Health':
    #                         player_health = Use_Potion.use_health_potion(player_health)
    #                     elif potion_to_use == 'Greater':
    #                         player_health = Use_Potion.use_greater_health_potion(player_health)
    #                     elif potion_to_use == 'Life':
    #                         player_health = Use_Potion.use_life_potion(player_health)
    #                     else:
    #                         print("Invalid input!")
    #                         continue
    #                     potion_inventory.remove(potion_to_use)
    #                     print(f"You healed to {player_health} HP.")
    #                 else:
    #                     print ("you have no more potions.")
    #                     continue

    if answer == 'fight':
           
        while (player_health > 0) and (monster_health > 0):
            
            print("""Magic | Melee | Special | Use Potion""")
            
            combat_choice = input("You must make a decision: ").lower()

            if combat_choice == 'magic':
                print("Your spell options are:")
                options = ['A','B','C','D']
                for options,each_spell in zip(options,player_character.spells):
                    print(f"""{options} - {each_spell}""")
                print ("\nMake your choice: ")
                
                spell_choice = input().lower()

                spell_hit = player_character.combat_magic_hit_modifier()
                spell_dmg = player_character.combat_magic_dmg_modifier(spell_choice)

                if spell_hit > 11:
                    print(f"Your ability connects! You deal {spell_dmg} damage!")
                    if monster_health <= spell_dmg:
                        monster_health = 0

                    elif monster_health > spell_dmg:
                        print(f"Your spell hits, but does not kill the monster!")
                        monster_health = monster_health - spell_dmg

                        time.sleep(1.5)

                        print("You must now ready yourself for a counter attack.")
                        
                        time.sleep(3)

                        player_health = defense_against_monster(player_character,player_health)
                        print(f"""You have {player_health} HP left. """)
                        time.sleep(1)

                else:
                    print(f"""You miss!""")
                    print("Prepare to defend yourself!")
                    
                    time.sleep(2)

                    player_health = defense_against_monster(player_character,player_health)
                    print(f"You have {player_health} HP left.")
                
            if combat_choice == 'melee':
                print('Your options are:')
                options = ['A','B','C','D']
                for options,each_ability in zip(options,player_character.weapon.abilities):
                    print(f"""{options} - {each_ability}""")
                    # print(each_ability, end ='  ')
                print("\nMake your choice. ")

                ability_choice = input().lower()

                ability_hit = player_character.combat_melee_hit_modifier()
                ability_dmg = player_character.weapon.melee_dmg(ability_choice)
                modifier = player_character.combat_melee_dmg_modifier(ability_choice)
                ability_dmg += modifier

                if ability_hit > 10:
                    print(f"Your weapon connects! You deal {ability_dmg}.")
                    if monster_health <= ability_dmg:
                        monster_health = 0
                    
                    elif monster_health > ability_dmg:
                        print("Your attack hits, but does not kill the enemy.")
                        monster_health = monster_health - ability_dmg

                        time.sleep(1.5)

                        print("Prepare for a counterattack!")

                        time.sleep(1.5)

                        player_health = defense_against_monster(player_character,player_health)
                        print(f" You have {player_health} HP left.")
                        time.sleep(1)
                    
                else:
                    print(f"""You miss!""")
                    time.sleep(1)

                print("Defend yourself!")
                
                time.sleep(2)

                player_health = defense_against_monster(player_character,player_health)
                print(f"You have {player_health} HP left.")

            if combat_choice == 'special':
                try:
                    special_ability, special_ability_description = player_character.weapon.get_special_ability()
                    # special_ability_description = player_character.weapon.special_ability_description
                    print(f"""Your weapon's special ability is:
{special_ability} - {special_ability_description}""")
                    time.sleep(.5)

                    use_spec_answer = input("Do you want to use it? ").lower()
                    if use_spec_answer == 'no':
                        continue
                    elif use_spec_answer == 'yes':
                        print(f"You use {special_ability.split(' - ')[0]}.")
                        # print(f"You use {special_ability}")
                        player_health, dmg = player_character.weapon.special_ability_actions(player_character, player_health)
                        if monster_health <= dmg:
                            monster_health = 0
                            break
                        
                        else:
                            monster_health -= dmg

                        time.sleep(1)

                        print("Your enemy moves to attack!")

                        time.sleep(1)

                        player_health = defense_against_monster(player_character,player_health)
                        print(f" You have {player_health} HP left.")
                        time.sleep(1)
                    
                except NotImplementedError:
                    print("Your weapon has no special ability!")
                    time.sleep(1)



               
                # defense_chance = random.randint (1,20)
                # dmg_to_player = random.randint (1,10)
                
                # if defense_chance == 20:
                #     dmg_to_player = 0
                #     print (f"""You take {dmg_to_player} damage!
                #         But don't rejoin too soon.
                #         Prepare your next move.""")

                # elif 9 < defense_chance < 20:
                #     dmg_to_player = dmg_to_player // 2
                #     player_health = player_health - dmg_to_player
                #     print(f"""You ready yourself for impact.
                #         You suffer {dmg_to_player} damage.""")
                    
                #     if player_health <= 0:
                #         print("You died.")
                #         break

                # if 2 <= defense_chance <= 9:
                #     dmg_to_player = dmg_to_player - 2
                #     player_health = player_health - dmg_to_player
                #     print(f"""You take a brutal blow and suffer {dmg_to_player} damage.""")

                #     if player_health <= 0:
                #         print("You died.")
                #         break

            if combat_choice == 'use potion':
                if len(potion_inventory) > 0:
                    print (potion_inventory)
                    potion_to_use = input("Which potion would you like to use?Type only the first word. ").title()
                    if potion_to_use == 'Minor':
                        player_health = Use_Potion.use_minor_health_potion(player_health)
                    elif potion_to_use == 'Health':
                        player_health = Use_Potion.use_health_potion(player_health)
                    elif potion_to_use == 'Greater':
                        player_health = Use_Potion.use_greater_health_potion(player_health)
                    elif potion_to_use == 'Life':
                        player_health = Use_Potion.use_life_potion(player_health)
                    else:
                        print("Invalid input!")
                        continue
                    potion_inventory.remove(potion_to_use)
                    output = f"You healed to {player_health} HP."
                else:
                    print ("you have no more potions.")
                    continue

    if player_health <= 0:
        print("You died.")
        return player_health, potion_inventory, item_inventory
    
    if monster_health <= 0:
        print("You survived this encounter and slayed the beast!")
        print(f"You are left with {player_health} hit points.")
        return player_health, potion_inventory, item_inventory


def medium_combat(player_health, player_character, potion_inventory, item_inventory):
    pass

def hard_combat(player_health, player_character, potion_inventory, item_inventory):
    pass

def boss_combat(player_health, player_character, potion_inventory, item_inventory, boss, boss_health):
    boss_entrance = f"You see the {boss} for the first time...."
    for character in boss_entrance:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)
    print('\n')

    time.sleep(1)

    answer = input('Do you fight or flee? ').lower()

    if answer == 'flee':
        flee_role = player_character.flee_attempt()
        if flee_role >= 18:
            escape = "You escape!"
            for character in escape:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
                print('\n')

        else:
            failed_escape = "Flee failed! Ready yourself for combat!"
            for character in failed_escape:
                if character == ' ':
                    time.sleep(.05)
                print (character,end='',flush=True)
                time.sleep(.05)
                print('\n')

    elif answer == 'fight':
           
        while (player_health > 0) and (boss_health > 0):
            
            print("""Magic | Melee | Special | Use Potion""")
            
            combat_choice = input("You must make a decision: ").lower()

            if combat_choice == 'magic':
                print("Your spell options are:")
                options = ['A','B','C','D']
                for options,each_spell in zip(options,player_character.spells):
                    print(f"""{options} - {each_spell}""")
                print ("\nMake your choice: ")
                
                spell_choice = input().title()

                spell_hit = player_character.combat_magic_hit_modifier()
                spell_dmg = player_character.combat_magic_dmg_modifier(spell_choice)

                if spell_hit >= 10:
                    print(f"You cast {spell_choice} and it connects! You deal {spell_dmg} damage!")
                    if boss_health <= spell_dmg:
                        boss_health = 0

                    elif boss_health > spell_dmg:
                        print(f"Your spell hits, but does not kill the monster!")
                        boss_health = boss_health - spell_dmg

                        time.sleep(1.5)

                        print("You must now ready yourself for a counter attack.")
                        
                        time.sleep(3)

                        player_health = defense_against_monster(player_character,player_health)
                        print(f"""You have {player_health} HP left. """)
                        time.sleep(1)

                else:
                    print(f"""You cast {spell_choice} but it misses!""")
                    print("Prepare to defend yourself!")
                    
                    time.sleep(2)

                    player_health = defense_against_monster(player_character,player_health)
                    print(f"You have {player_health} HP left.")
                
            if combat_choice == 'melee':
                print('Your options are:')
                for each_ability in player_character.weapon.abilities:
                    print(each_ability, end ='  ')
                print("\nMake your choice. ")

                ability_choice = input().title()

                ability_hit = player_character.combat_melee_hit_modifier()
                ability_dmg = player_character.weapon.melee_dmg(ability_choice)
                modifier = player_character.combat_melee_dmg_modifier(ability_choice)
                ability_dmg += modifier

                if ability_hit > 10:
                    print(f"{ability_choice} connects! You deal {ability_dmg}.")
                    if boss_health <= ability_dmg:
                        boss_health = 0
                    
                    elif boss_health > ability_dmg:
                        print("Your attack hits, but does not kill the enemy.")
                        boss_health = boss_health - ability_dmg

                        time.sleep(1.5)

                        print("Prepare for a counterattack!")

                        time.sleep(1.5)

                        player_health = defense_against_monster(player_character,player_health)
                        print(f" You have {player_health} HP left.")
                        time.sleep(1)
                    
                else:
                    print(f"""{ability_choice} misses!""")
                    time.sleep(1)

                print("Defend yourself!")
                
                time.sleep(2)

                player_health = defense_against_monster(player_character,player_health)
                print(f"You have {player_health} HP left.")

            if combat_choice == 'special':
                try:
                    special_ability, special_ability_description = player_character.weapon.get_special_ability()
                    print(f"""Your weapon's special ability is:
{special_ability} - {special_ability_description}""")
                    time.sleep(.5)

                    use_spec_answer = input("Do you want to use it? ").lower()
                    if use_spec_answer == 'no':
                        continue
                    elif use_spec_answer == 'yes':
                        print(f"You use {special_ability.split(' - ')[0]}.")
                        player_health, dmg = player_character.weapon.special_ability_actions(player_character, player_health)
                        if boss_health <= dmg:
                            boss_health = 0
                            break
                        
                        else:
                            boss_health -= dmg

                        time.sleep(1)

                        print("Your enemy moves to attack!")

                        time.sleep(1)

                        player_health = defense_against_monster(player_character,player_health)
                        print(f" You have {player_health} HP left.")
                        time.sleep(1)
                    
                except NotImplementedError:
                    print("Your weapon has no special ability!")
                    time.sleep(1)

            if combat_choice == 'use potion':
                if len(potion_inventory) > 0:
                    print (potion_inventory)
                    potion_to_use = input("Which potion would you like to use? Type only the first word. ").title()
                    if potion_to_use == 'Minor':
                        player_health = Use_Potion.use_minor_health_potion(player_health)
                    elif potion_to_use == 'Health':
                        player_health = Use_Potion.use_health_potion(player_health)
                    elif potion_to_use == 'Greater':
                        player_health = Use_Potion.use_greater_health_potion(player_health)
                    elif potion_to_use == 'Life':
                        player_health = Use_Potion.use_life_potion(player_health)
                    else:
                        print("Invalid input!")
                        continue
                    potion_inventory.remove(potion_to_use)
                    print(f"You healed to {player_health} HP.")
                else:
                    print ("You have no more potions.")
                    continue

    if player_health <= 0:
        print("You died.")
        return player_health, potion_inventory, item_inventory
    
    if boss_health <= 0:
        return player_health, potion_inventory, item_inventory



