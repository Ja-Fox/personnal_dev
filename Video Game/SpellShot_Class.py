import random
import time
import Weapon_Classes

class Spell_Shot:

    def __init__(self,player_name,attributes,starting_health = 20):
        self.player_name = player_name
        self.attributes = attributes
        self.starting_health = starting_health

        self.spells = ['Rapid Fire','Aether Bolt', 'Bramblethorn']
        text = f"As a Spellshot, you can use the following abilities:"
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

        self.armor_type = "medium"
        text2 = f"""You have a {self.armor_type} armor class."""
        for character in text2:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')
        text3 = f"You wield a novice-level shortbow.\n"
        for character in text3:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        self.weapon = Weapon_Classes.Shortbow('Brightmoon Bow',1)
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
Rapid Fire - Quickfire your bow, firing a volley of arrows toward your target
Aether Bolt - Focus and imbue your shot with magic energy
Bramblethorn - Summon lashing vines form the earth to strike at your enemy
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
            dmg1 = random.randint(2,5)
            dmg2 = random.randint(2,5)
            dmg3 = random.randint(2,5)
            dmg = dmg1 + dmg2 + dmg3

            if self.attributes['Dexterity'] > 16:
                dmg = dmg + random.randint(2,5)
            elif 10 <= self.attributes['Dexterity'] <= 16:
                dmg = dmg + random.randint(2,4)
            else:
                dmg = dmg + random.randint(1,3)
            print(f"You hit for {dmg1}")
            time.sleep(1)
            print(f"You hit for {dmg2}")
            time.sleep(1)
            print(f"You hit for {dmg3}")
            time.sleep(1)
            return dmg

        elif spell_choice == 'b':
            dmg = random.randint(3,10)
            if self.attributes['Wisdom'] > 16:
                dmg += random.randint(5,9)
            elif 10 <= self.attributes['Dexterity'] <= 16:
                dmg += random.randint(2,5)
            else:
                dmg += random.randint(1,3)
            return dmg

        elif spell_choice == 'c':
            dmg = random.randint(5,12)

            if self.attributes['Wisdom'] > 16:
                dmg = dmg + random.randint(3,10)
            elif 10 <= self.attributes['Wisdom'] <= 16:
                dmg = dmg + random.randint(2,6)
            else:
                dmg = dmg + random.randint(2,4)
            return dmg          
           
    def combat_magic_hit_modifier(self):
        spell_hit = random.randint(1,20)

        if self.attributes['Dexterity'] > 16:
            spell_hit += 3
        elif 10 <= self.attributes['Dexterity'] <= 16:
            spell_hit += 2
        else:
            spell_hit += 1

        if self.attributes['Wisdom'] > 16:
            spell_hit += 3
        elif 10 <= self.attributes['Wisdom'] <= 16:
            spell_hit += 2
        else:
            spell_hit += 1

        return spell_hit

    def combat_melee_dmg_modifier(self,ability_choice):
        if ability_choice  =='a':
            mod = random.randint(4,8)
            if self.attributes['Wisdom'] > 16:
                mod += 3
            elif 10 <= self.attributes['Wisdom'] <= 16:
                mod += 2
            else:
                return mod
            return mod   

        if ability_choice == 'b':
            mod = random.randint(1,10)
            if self.attributes['Dexterity'] > 16:
                mod = mod + random.randint(2,9)
            elif 10 <= self.attributes['Dexterity'] <= 16:
                mod = mod + random.randint(1,7)
            else:
                mod = mod + random.randint(1,4)
            return mod
        
        if ability_choice == 'c':
            mod = random.randint(1,8)
            if self.attributes['Dexterity'] > 16:
                mod = mod + random.randint(3,10)
            elif 10 <= self.attributes['Dexterity'] <= 16:
                mod = mod + random.randint(2,7)
            else:
                mod += 2
            return mod
    
    def combat_melee_hit_modifier(self):
        ability_hit = random.randint(1,20)

        if self.attributes['Dexterity'] > 16:
            ability_hit += 2
        elif 10 <= self.attributes['Dexterity'] <= 16:
            ability_hit += 1
        else:
            ability_hit = ability_hit

        if self.attributes['Wisdom'] > 16:
            ability_hit += 2
        elif 10 <= self.attributes['Wisdom'] <= 16:
            ability_hit += 1
        else:
            ability_hit = ability_hit

        return ability_hit

    def defense_against_attack(self):
        defense_roll = random.randint(1,12)

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
            defense_roll += 2
        elif 13 <= self.attributes[con] < 16:
            defense_roll += 1
        else:
            defense_roll += 0

        defense_roll += armor_bonus
        return defense_roll
    
    def flee_attempt(self):
        flee_role = (random.randint(1,20))
        dex = 'Dexterity'

        if self.attributes[dex] >= 16:
            flee_role += 3
        elif 13 <= self.attributes[dex] < 16:
            flee_role += 2
        elif 10 <= self.attributes[dex] <= 12:
            flee_role += 1
        else:
            flee_role += 0
        
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



