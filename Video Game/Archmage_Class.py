import random
import time
import Weapon_Classes

class Archmage:

    def __init__(self,player_name,attributes,starting_health=20):
        self.player_name = player_name
        self.attributes = attributes
        self.starting_health = starting_health

        self.spells = ['Firebolt','Lightning Strike','Frostbite', 'Howling Gale']
        text = f"As an Archmage, you have the follwing spells in your aresenal:\n"
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')
        for each_spell in self.spells:
            print(each_spell)
        time.sleep(4)
        print('\n')

        self.armor_type = "light"
        text2 = f"""
You are dressed in spellcaster attire and have a {self.armor_type} armor class.
This will not afford you much protection against enemies. Perhaps your spell power
will make up for it."""
        for character in text2:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')
        text3 = f"You wield a novice-level mage's staff.\n"
        for character in text3:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        self.weapon = Weapon_Classes.Novice_Staff('Sunder',1)
        text4 = f"Your weapon affords you following abilities:"
        for character in text4:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print(f"""
{self.weapon.abilities[0]}
{self.weapon.abilities[1]}
{self.weapon.abilities[2]}""")
        time.sleep(3)
        print('\n')

    def ability_descriptions(self):
        print(f""" 
Firebolt - Quickly conjure and throw a mote of flame at your enemy.
Lightning Strike - Harness the power of the elements and fire a bolt of lightning from your staff
Frostbite - Freeze your target momentarily
Howling Gale - Batter your target with harsh winds
""")

    def chance_to_evade(self):
        evasion_roll = random.randint (1,16)
        dex = 'Dexterity'
        luck = 'Luck'

        if self.attributes[dex] >= 16:
            evasion_roll += 3
        elif 13 <= self.attributes[dex] < 16:
            evasion_roll += 2
        elif 10 <= self.attributes[dex] <= 12:
            evasion_roll += 1
        else:
            evasion_roll += 0
        
        if self.attributes[luck] >= 16:
            evasion_roll += 2
        elif 13 <= self.attributes[luck] < 16:
            evasion_roll += 1
        else:
            evasion_roll += 0

        return evasion_roll
     
    def check_health(self):
        pass

    def combat_magic_dmg_modifier(self,spell_choice):
        if spell_choice =='a':
            dmg = random.randint(2,6)

            if self.attributes['Intelligence'] > 16:
                dmg = dmg + random.randint(3,8)
            elif 10 <= self.attributes['Intelligence'] <= 16:
                dmg = dmg + random.randint(2,5)
            else:
                dmg = dmg + random.randint(1,4)


        elif spell_choice == 'b':
            dmg = random.randint(2,10)
            if self.attributes['Intelligence'] > 16:
                dmg = dmg + random.randint(2,9)
            elif 10 <= self.attributes['Intelligence'] <= 16:
                dmg = dmg + random.randint(1,7)
            else:
                dmg = dmg + random.randint(1,4)
        
        elif spell_choice == 'c':
            dmg = random.randint(2,12)

            if self.attributes['Intelligence'] > 16:
                dmg = dmg + random.randint(3,10)
            elif 10 <= self.attributes['Intelligence'] <= 16:
                dmg = dmg + random.randint(2,7)
            else:
                dmg = dmg + random.randint(2,4)
        
        elif spell_choice == 'd':
            dmg = random.randint(2,8)

            if self.attributes['Intelligence'] > 16:
                dmg = dmg + random.randint(3,10)
            elif 10 <= self.attributes['Intelligence'] <= 16:
                dmg = dmg + random.randint(2,7)
            else:
                dmg = dmg + random.randint(2,4)

        return dmg
    
    def combat_magic_hit_modifier(self):
        spell_hit = random.randint(1,20)

        if self.attributes['Intelligence'] > 16:
            spell_hit += 3
        elif 10 <= self.attributes['Intelligence'] <= 16:
            spell_hit += 2
        else:
            spell_hit += 1

        if self.attributes['Wisdom'] > 16:
            spell_hit += 2
        elif 10 <= self.attributes['Wisdom'] <= 16:
            spell_hit += 1
        else:
            spell_hit = spell_hit

        return spell_hit

    def combat_melee_dmg_modifier(self,ability_choice):
        if (ability_choice  =='a'):
        # or (ability_choice == 'b') or (ability_choice == 'c') or (ability_choice == 'd'):
            mod = random.randint(1,5)
            if self.attributes['Strength'] > 16:
                mod += 3
            elif 10 <= self.attributes['Strength'] <= 16:
                mod += 2
            else:
                mod = mod
            return mod   

        if ability_choice == 'b':
            mod = random.randint(1,10)
            if self.attributes['Strength'] > 16:
                mod = mod + random.randint(2,9)
            elif 10 <= self.attributes['Strength'] <= 16:
                mod = mod + random.randint(1,7)
            else:
                mod = mod + random.randint(1,4)
            return mod
        
        if ability_choice == 'c':
            mod = random.randint(1,8)
            if self.attributes['Strength'] > 16:
                mod = mod + random.randint(3,10)
            elif 10 <= self.attributes['Strength'] <= 16:
                mod = mod + random.randint(2,7)
            else:
                mod += 2
            return mod
        
        if ability_choice == 'd':
            mod = random.randint(1,8)
            if self.attributes['Strength'] > 16:
                mod = mod + random.randint(3,10)
            elif 10 <= self.attributes['Strength'] <= 16:
                mod = mod + random.randint(2,7)
            else:
                mod += 2
            return mod

    def combat_melee_hit_modifier(self):
        ability_hit = random.randint(1,20)

        if self.attributes['Strength'] > 16:
            ability_hit += 2
        elif 10 <= self.attributes['Strength'] <= 16:
            ability_hit += 1
        else:
            ability_hit = ability_hit

        if self.attributes['Dexterity'] > 16:
            ability_hit += 2
        elif 10 <= self.attributes['Dexterity'] <= 16:
            ability_hit += 1
        else:
            ability_hit = ability_hit

        return ability_hit

    def defense_against_attack(self):
        defense_roll = random.randint(1,15)

        if self.armor_type == "light":
            armor_bonus = 1
        if self.armor_type =="medium":
            armor_bonus = 2
        if self.armor_type == "heavy":
            armor_bonus = 3
                
        str = 'Strength'
        con = 'Constitution'

        if self.attributes[str] >= 16:
            defense_roll += 3
        elif 13 <= self.attributes[str] < 16:
            defense_roll += 2
        elif 10 <= self.attributes[str] <= 12:
            defense_roll += 1
        else:
            defense_roll += 0
        
        if self.attributes[con] >= 16:
            defense_roll += 3
        elif 11 <= self.attributes[con] < 16:
            defense_roll += 2
        else:
            defense_roll += 0

        defense_roll += armor_bonus
        return defense_roll

    def flee_attempt(self):
        flee_role = (random.randint(1,20))
        dex = 'Dexterity'
        if self.attributes[dex] >= 16:
            flee_role += 5

        elif 13 <= self.attributes[dex] < 16:
            flee_role += 3

        elif 10 <= self.attributes[dex] <= 12:
            flee_role += 2

        else:
            flee_role += 1
        
        return flee_role

    def starting_player_health(self):
        const = 'Constitution'
        if self.attributes[const] >= 16:
            self.starting_health += 20

        elif 13 <= self.attributes[const] < 16:
            self.starting_health += 10

        elif 10 <= self.attributes[const] <= 12:
            self.starting_health += 6

        else:
            self.starting_health += 3

        text=f"You begin your journey with {self.starting_health} hit points."
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        time.sleep(3)
        print('\n')
        return self.starting_health










