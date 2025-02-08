import random
import time

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_special_ability(self):
        raise NotImplementedError("Subclasses must implement this method")

    def special_ability_actions(self, player_character, player_health):
        raise NotImplementedError("Subclasses must implement this method")
 
#################################################################################
######### This section contains all subclasses of Staff

class Staff(Weapon):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        self.abilities = ['Pummel','Twin Strike',"Crushing Blow"]

class Novice_Staff(Staff):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.name = name
        self.damage = damage
        self.abilities = ['Pummel','Twin Strike', "Crushing Blow"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Acid Splash":'Hurl a bubble of acid at your target.',
    "Conjuer: Spectral Sword":'Summon a scimitar from the aether, willing it to attack your target.',
    'Earthen Tremor':'You cause a minor earthquake in your vicinity, damaging enemies around you.'
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Acid Splash":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Conjuer: Spectral Sword":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Earthen Tremor":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):

        if ability_choice  == 'a': ## A = Pummel
            dmg = random.randint(1,7)
            return dmg 

        elif ability_choice == 'b': ## B = Twin Strike
            dmg = random.randint(1,7)
            return dmg

        elif ability_choice == 'b': ## C = Crushing Blow
            dmg = random.randint(1,7)
            return dmg

        else:
            return 0

class Adept_Staff(Staff):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.name = name
        self.damage = damage
        self.abilities = ['Pummel','Twin Strike', "Crushing Blow"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Mending":'Instantly heal yourself for a small amount.',
    "Conjuer: Spectral Axe":'Summon an axe from the aether, willing it to attack your target.',
    'Emberstorm':'You create a sphere of swirling fire, centering on you.'
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        
        if ability_option == "Emberstorm":
            dmg = random.randint(1,9)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 3
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 2
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

        if ability_option == "Conjuer: Spectral Axe":
            dmg = random.randint(1,10)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 4
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 2
            else:
                dmg += 0 
            print(f"Your Spectral Axe does {dmg} points of damage.")
            return player_health, dmg

        if ability_option == "Mending":
            dmg = 0
            healing  = random.randint(1,10)
            player_health += healing
            print(f"You heal for {healing}.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):

        if ability_choice  == 'a': ## A = Pummel
            dmg = random.randint(1,8)
            return dmg 

        elif ability_choice == 'b': ## B = Twin Strike
            dmg = random.randint(1,8)
            return dmg

        elif ability_choice == 'c': ## C = Crushing Blow
            dmg = random.randint(1,8)
            return dmg

        else:
            return 0
        
class Journeyman_Staff(Staff):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Pummel','Twin Strike','Crushing Blow']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Winter's Grasp":'You summon a numbing frost storm around target and deal two rounds of cold damage.',
    'Thunderclap':'You create a sonic boom to blast enemies.',
    "Summon: Spectral Glaive":"Send a glaive from the aether at your target, damaging your target going out and when return to you.",
    "Chromatic Orb":"Generate a sphere of energy and fire it at your target with brilliantly bright light.",
    }
    
        rand_abil = random.choice(list(ability_options.keys()))
        return rand_abil, ability_options[rand_abil]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Winter's Grasp":
            dmg1 = random.randint(2,7)

            if player_character.attributes['Intelligence'] > 16:
                dmg1 = dmg1 + 4
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg1 = dmg1 + 3
            else:
                dmg1 += 0 
            print(f"Winter's Grasp does {dmg1}")

            dmg2 = random.randint(2,7)
            if player_character.attributes['Intelligence'] > 16:
                dmg2 = dmg2 + 2
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg2 = dmg2 + 1
            else:
                dmg2 += 0 
            print(f"Winter's Grasp does {dmg2}")

            total = dmg1 + dmg2
            return player_health, total

        if ability_option == "Thunderclap":
            dmg = random.randint(4,12)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 4
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 3
            else:
                dmg = dmg
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

        if ability_option == "Summon: Spectral Glaive":
            dmg1 = random.randint(2,7)

            if player_character.attributes['Intelligence'] > 16:
                dmg1 = dmg1 + 4
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg1 = dmg1 + 3
            else:
                dmg1 += 0 
            print(f"You command your Glaive toward your target, dealing {dmg1} points of damage, and command it back.")

            dmg2 = random.randint(2,7)
            if player_character.attributes['Intelligence'] > 16:
                dmg2 = dmg2 + 2
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg2 = dmg2 + 1
            else:
                dmg2 += 0 
            print(f"It deals {dmg2} points of damage as it returns to you.")

            total = dmg1 + dmg2
            return player_health, total

        if ability_option == "Chromatic Orb":
            dmg = random.randint(3,9)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 4
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 3
            else:
                dmg = dmg
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):

        if ability_choice  == 'a': ## a = Pummel
            dmg = random.randint(1,9)
            return dmg 

        elif ability_choice == 'b': ## b = Twin Strike
            dmg = random.randint(1,9)
            return dmg

        elif ability_choice == 'b': ## c = Crushing Blow
            dmg = random.randint(1,9)
            return dmg

        else:
            return 0

class Master_Staff(Staff):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Pummel','Twin Strike','Crushing Blow']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    'Sunburst':'Brilliant sunfire flahes across the battlefield, emenating from you, and burning enemies.',
    "Volt Crash":"Channel a bolt of lightning through your staff, overloading the target with 3 rounds of lightning damage.",
    "Event Horizon":"Generate a singularity at your target's position, crushing them with an instant kill chance.",
    "Cryosphere":"Act as a conduit for the God of Winter, allowing your surrounding area to freeze and do heavy cold damage to your target."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Sunburst":
            dmg = random.randint(6,19)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 5
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 3
            else:
                dmg = dmg
            print(f"You burn your enemy for {dmg} points of their health.")
            return player_health, dmg
        
        if ability_option == "Event Horizon":
            dmg = random.randint(6,18)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("Your target is drawn in passed the event horizon and is banished into another dimension.")
            elif kill < 19:
                if player_character.attributes['Intelligence'] > 16:
                    dmg = dmg + 5
                elif 10 <= player_character.attributes['Intelligence'] <= 16:
                    dmg = dmg + 3
                else:
                    dmg += 0 
            print(f"Your singularity does not kill your target, but does deal {dmg} points of damage.")
            return player_health, dmg

        if ability_option == "Cryosphere":
            dmg = random.randint(8,19)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 6
            else:
                dmg = dmg
            print(f"As you sever the connection to the Gods, your spell deals {dmg} points of damage.")
            return player_health, dmg
     
        if ability_option == "Volt Crash":
            dmg1 = random.randint(1,9)
            if player_character.attributes['Intelligence'] > 16:
                dmg1 += 5
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg1 += 3
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of electric damage!")
            time.sleep(1)

            dmg2 = random.randint(1,9)
            if player_character.attributes['Intelligence'] > 16:
                dmg2  += 5
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg2 += 3
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of electric damage!")
            time.sleep(1)

            dmg3 = random.randint(1,9)
            if player_character.attributes['Intelligence'] > 16:
                dmg3 += 5
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg3 += 3
            else:
                dmg3 += 0
            print(f"You do {dmg3} points of electric damage!")
            time.sleep(1)

            total = dmg1 + dmg2 + dmg3
            print(f"You cease your channeling, having done {total} points of damage.")
            return player_health, total

    def melee_dmg(self,ability_choice):

        if ability_choice  == 'a': ## a = Pummel
            dmg = random.randint(1,10)
            return dmg 

        elif ability_choice == 'b': ## b = Twin Strike
            dmg = random.randint(1,10) 
            return dmg

        elif ability_choice == 'c': ## c = Crushing Blow
            dmg = random.randint(1,10)
            return dmg

        else:
            return 0

class Archmage_Staff(Staff):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Pummel','Twin Strike','Crushing Blow']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')
        
    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Metor Crash":'Call a meteor down from the heavens, dealing immense fire and bludgeoning damage if it hits.',
    "Absolute Zero":'Bring your targets body temperature down to absolute zero for a brief time. This ability has a chance of instantly killing the target.',
    'Regenerate':'Concentrate your power into healing energy. Heal for a portion of missing health over time.',
    'Scatter the Weak':'Summon the immense energy you control to blast your target with arcance energy. This spell instantly kills your target, but exacts a toll on you as well.'
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == 'Meteor Crash':
            dmg = random.randint(8,25)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg = dmg + 6
            else:
                dmg += 0
            return player_health, dmg

        if ability_option == 'Absolute Zero':
            dmg = random.randint(1,25)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("You freeze your target solid, killing it instantly.")
            elif kill < 19:
                if player_character.attributes['Intelligence'] > 16:
                    dmg = dmg + 8
                elif 10 <= player_character.attributes['Intelligence'] <= 16:
                    dmg = dmg + 6
                else:
                    dmg += 0 
            return player_health, dmg

        if ability_option == 'Regenerate':
            dmg = 0
            healing  = random.randint(1,25)
            player_health += healing
            print(f"You heal for {healing}.")
            return player_health, dmg

        if ability_option == 'Scatter the Weak':
            dmg = 100000000
            degen = random.randint(3,15)
            player_health -= degen
            print(f"You sacrafice {degen} hit points.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):

        if ability_choice  == 'a': ## a = Pummel
            dmg = random.randint(1,11)
            return dmg 

        elif ability_choice == 'b': ## b = Twin Strike
            dmg = random.randint(1,11)
            return dmg

        elif ability_choice == 'c': ## c = Crushing Blow
            dmg = random.randint(1,11)
            return dmg

class Ritualist_Staff(Staff):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Pummel','Twin Strike','Crushing Blow']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    'Soul Bind':"Force the target's soul to lose connection with its physical body. This ability has a chance of eternally paralyzing the target -- this does not kill the target.",
    "Voidwalk":"Commune with the Beyond and move through it to attack your target's spirit. This attack is unblockable and has a chance of instantly killing the target, but the Beyond takes its toll on your spirit.",
    'Ray of Enfeeblement':'Concentrate and channel an ethereal energy blast at youre target. This spell can do up to 4 consecutive rounds of necrotic damage.',
    "Icingdeath's Frost":"Call a burst of chilling energy from the Beyond at your target. This spell deals one round of cold damage, and another round of necrotic damage.",
    'Breathe of Life':'Appeal to the spririts for a gift of life. immediately for a portion of your missing health.',
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Soul Bind":
            dmg = random.randint(5,25)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("The target's soul is lost to the aether..its body falls to the ground.")
            elif kill < 19:
                if player_character.attributes['Intelligence'] > 16:
                    dmg += 8
                elif 10 <= player_character.attributes['Intelligence'] <= 16:
                    dmg += 6
                else:
                    dmg += 0 
            return player_health, dmg
        
        if ability_option == "Icingdeath's Frost":
            dmg1 = random.randint(1,10)
            if player_character.attributes['Intelligence'] > 16:
                dmg1 += 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg1 += 6
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of cold damage!")
            
            dmg2 = random.randint(1,12)
            if player_character.attributes['Intelligence'] > 16:
                dmg2  += 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg2 += 6
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of necrotic damage!")

            total = dmg1 + dmg2
            return player_health, total
        
        if ability_option == "Ray of Enfeeblement":
            dmg1 = random.randint(1,8)
            if player_character.attributes['Intelligence'] > 16:
                dmg1 += 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg1 += 6
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of necrotic damage!")
            
            dmg2 = random.randint(1,8)
            if player_character.attributes['Intelligence'] > 16:
                dmg2  += 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg2 += 6
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of necrotic damage!")

            dmg3 = random.randint(1,8)
            if player_character.attributes['Intelligence'] > 16:
                dmg3 += 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg3 += 6
            else:
                dmg3 += 0
            print(f"You do {dmg3} points of necrotic damage!")

            dmg4 = random.randint(1,8)
            if player_character.attributes['Intelligence'] > 16:
                dmg4 += 8
            elif 10 <= player_character.attributes['Intelligence'] <= 16:
                dmg4 += 6
            else:
                dmg4 += 0
            print(f"You do {dmg4} points of necrotic damage!")
            
            
            total = dmg1 + dmg2 + dmg3 + dmg4
            return player_health, total

        if ability_option == "Breathe of Life":
            dmg = 0
            healing  = random.randint(6,25)
            player_health += healing
            print(f"You heal for {healing}.")
            return player_health, dmg

        if ability_option == "Voidwalk":
            dmg = random.randint(6,25)
            degen = random.randint(3,10)
            player_health -= degen 

            kill = random.randint(1,20)
            if kill >= 18:
                dmg = 100000000
                print("You tear the soul from target, killing it instantly.")
                return player_health, dmg

            elif kill < 19:
                if player_character.attributes['Intelligence'] > 16:
                    dmg += 8
                elif 10 <= player_character.attributes['Intelligence'] <= 16:
                    dmg += 6
                else:
                    dmg += 0 
            print(f"You deal {dmg} points of damage.")
            time.sleep(1.5)
            print(f"The Beyond exacts its toll of {degen} hit points.")
            return player_health, dmg
            
    def melee_dmg(self,ability_choice):

        if ability_choice  == 'Pummel':
            dmg = random.randint(1,11)
            return dmg 

        elif ability_choice == 'Twin Strike':
            dmg = random.randint(1,11)
            return dmg

        elif ability_choice == 'Crushing Blow':
            dmg = random.randint(1,11)
            return dmg

        else:
            return 0


#################################################################################
######### This section contains all subclasses of Sword

class Sword(Weapon):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        self.abilities = ['Crosscut','Punishing Blow','Hamstring']

class Gladius(Sword):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Focused Strike','Punishing Blow','Hamstring']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Umbral Slash":"Merge with the shadows, lunging to cut at you target.",
    "Warfury":"Become one with the Heart of Battle and lash out at your target.",
    "Warpath":"Charge your target, dealing initial blunt damage. Then swing your weapon for slashing damage."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Umbral Slash":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Warfury":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Warpath":
            dmg = random.randint(2,6)
            dmg2 = dmg - 1

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You charge your for, connecting for {dmg} points of damage.")
            time.sleep(1)
            print(f"You follow up with a swing of your sword, dealing {dmg2} damage!")
            total = dmg + dmg2
            return player_health, total

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Strike
            dmg = random.randint(1,7)
            return dmg 

        elif ability_choice == 'b': ## b = Punishing Blow
            dmg = random.randint(1,7)
            return dmg

        elif ability_choice == 'c': ## c = Hamstring
            dmg = random.randint(1,7)
            return dmg

class Sabre(Sword):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Focused Strike','Punishing Blow','Hamstring']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Cleave":"Hack at your target with readied power.",
    "Tactician's Thrust":"Identify your target's weak point and thrust your weapon at that spot.",
    "Frenzied Assault":"Your vision goes red as you become one with the Heart of Battle and attack your target with unrelenting force.",
    "Valorous Stab":"Ready your blade and strike true."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Cleave":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Tactician's Thrust":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Frenzied Assault":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        
        if ability_option == "Valorous Stab":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Strike
            dmg = random.randint(1,8)
            return dmg 

        elif ability_choice == 'b': ## b = Punishing Blow
            dmg = random.randint(1,8)
            return dmg

        elif ability_choice == 'c': ## c = Hamstring
            dmg = random.randint(1,8)
            return dmg

        else:
            return 0

class Longsword(Sword):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Focused Strike','Punishing Blow','Hamstring']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Triumphant Swing":"Unleash a powerful swing that carries the momentum of Victory.",
    "Out for Blood":"Pursue your target with relentless determination, damaging your target and healing for a small amount.",
    "Annihilation":"Attempt to obilerate your target. Even on failed destruction, your target takes heavy damage.",
    "Echoing Strike":"Move as if you were an echo of time, striking your opponent with three consecutive blows."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Triumphant Swing":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Out for Blood":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Annihilation":
            dmg = random.randint(6,18)
            kill = random.randint(1,20)

            if kill == 20:
                dmg = 100000000
                print("You destroyed your target.")
            elif kill < 20:
                if player_character.attributes['Strength'] > 16:
                    dmg = dmg + 5
                elif 10 <= player_character.attributes['Strength'] <= 16:
                    dmg = dmg + 3
                else:
                    dmg += 0 
            print(f"You do not kill your target, but it takes {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Echoing Strike":
            dmg1 = random.randint(1,10)
            if player_character.attributes['Strength'] > 16:
                dmg1 += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg1 += 6
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of damage!")
            time.sleep(1)

            dmg2 = random.randint(1,12)
            if player_character.attributes['Strength'] > 16:
                dmg2  += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg2 += 6
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of damage!")
            time.sleep(1)

            dmg3 = random.randint(1,12)
            if player_character.attributes['Strength'] > 16:
                dmg3  += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg3 += 6
            else:
                dmg3 += 0
            print(f"You do {dmg3} points of damage!")
            time.sleep(1)

            total = dmg1 + dmg2 + dmg3
            return player_health, total

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Strike
            dmg = random.randint(1,9)
            return dmg 

        elif ability_choice == 'b': ## b = Punishing Blow
            dmg = random.randint(1,9)
            return dmg

        elif ability_choice == 'c': ## c = Hamstring
            dmg = random.randint(1,9)
            return dmg

        else:
            return 0

class Broadsword(Sword):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Focused Strike','Punishing Blow','Hamstring']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Warlord's Fury":"Channel your raw fury, striking your enemy with a devestating blow and healing for a percentage of the damage.",
    "Whirlwind Blade":"Spin 4 times in place, slashing enemies in your vicinity.",
    "Warpath":"Attack your target, first landing a front kick, followed by a vicious stab of your sword."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Warlord's Fury":
            dmg = random.randint(6,15)

            if player_character.attributes['Strength'] > 16:
                dmg += 3
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            time.sleep(1.5)
            heal = dmg // 2
            player_health += heal
            print(f"You heal for {heal} hit points!")
            return player_health, dmg
        
        if ability_option == "Whirlwind Blade":
            dmg1 = random.randint(1,9)
            if player_character.attributes['Strength'] > 16:
                dmg1 += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg1 += 6
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of damage!")
            time.sleep(1)

            dmg2 = random.randint(1,12)
            if player_character.attributes['Strength'] > 16:
                dmg2  += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg2 += 6
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of damage!")
            time.sleep(1)

            dmg3 = random.randint(1,9)
            if player_character.attributes['Strength'] > 16:
                dmg3  += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg3 += 6
            else:
                dmg3 += 0
            print(f"You do {dmg3} points of damage!")
            time.sleep(1)

            dmg4 = random.randint(1,12)
            if player_character.attributes['Strength'] > 16:
                dmg4  += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg4 += 6
            else:
                dmg4 += 0
            print(f"You do {dmg4} points of damage!")
            time.sleep(1)

            total = dmg1 + dmg2 + dmg3 + dmg4
            return player_health, total
        
        if ability_option == "Warpath":
            dmg1 = random.randint(1,10)
            if player_character.attributes['Strength'] > 16:
                dmg1 += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg1 += 6
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of damage!")
            time.sleep(1)

            dmg2 = random.randint(1,12)
            if player_character.attributes['Strength'] > 16:
                dmg2  += 8
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg2 += 6
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of damage!")
            time.sleep(1)

            total = dmg1 + dmg2
            return player_health, total

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Strike
            dmg = random.randint(1,10)
            return dmg 

        elif ability_choice == 'b': ## b = Punishing Blow
            dmg = random.randint(1,10)
            return dmg

        elif ability_choice == 'c': ## c = Hamstring
            dmg = random.randint(1,10)
            return dmg

        else:
            return 0

class Greatsword(Sword):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Focused Strike','Punishing Blow','Hamstring']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Siegebreaker":"Empower your next attack, seeking to break your target's defenses. This ability has a chance of breaking your target's defense, killing it instantly. ",
    "Fury's Conduit":"You become a conduit of the God of War and attack your target with unrelenting force and enhance your damage.",
    "Legionnaire's Stand":"Strike fast and ready your defenses for the oncoming attack, significantly reducing the next round of incoming damage.",
    "Seige Engine":"Become an engine of destruction as your charge your target. You deal one round of bludgeoning damage, and successive rounds of explosive energy as you seek to destroy your foe."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability

        if ability_option == "Siegebreaker":
            dmg = random.randint(1,25)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("You strike your target with unending force, breaking their will and killing it instantly.")
            elif kill < 19:
                if player_character.attributes['Strength'] > 16:
                    dmg = dmg + 8
                elif 10 <= player_character.attributes['Strength'] <= 16:
                    dmg = dmg + 6
                else:
                    dmg += 0 
                print(f"You do not break your target, but you do deal {dmg} points of damage.")
            return player_health, dmg

        if ability_option == "Fury's Conduit":
            dmg = random.randint(6,17)
            multi = random.randint(2,4)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 5
            else:
                dmg += 0
            
            total = dmg * multi
            print(f"The God of War enhances your strength {multi} fold, increasing your damage to {total}.")
            return player_health, total
        
        if ability_option == "Legionnaire's Stand":
            dmg = random.randint(6,19)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            # somehow reduce damage next round?
            return player_health, dmg

        if ability_option == "Seige Engine":
            dmg1 = random.randint(1,9)
            if player_character.attributes['Strength'] > 16:
                dmg1 += 5
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg1 += 3
            else:
                dmg1 += 0
            print(f"You do {dmg1} points of bludgeoning damage!")
            time.sleep(1)

            dmg2 = random.randint(1,9)
            if player_character.attributes['Strength'] > 16:
                dmg2  += 5
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg2 += 3
            else:
                dmg2 += 0
            print(f"You do {dmg2} points of energy damage!")
            time.sleep(1)

            dmg3 = random.randint(1,9)
            if player_character.attributes['Strength'] > 16:
                dmg3 += 5
            elif 10 <= player_character.attributes['Strength'] <= 16:
                dmg3 += 3
            else:
                dmg3 += 0
            print(f"You do {dmg3} points of energy damage!")
            time.sleep(1)

            total = dmg1 + dmg2 + dmg3
            print(f"You end your assault, having inflicted {total} points of damage.")
            return player_health, total

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Strike
            dmg = random.randint(1,11)
            return dmg 

        elif ability_choice == 'b': ## b = Punishing Blow
            dmg = random.randint(1,11)
            return dmg

        elif ability_choice == 'c': ## c = Hamstring
            dmg = random.randint(1,11)
            return dmg

        else:
            return 0

#################################################################################
######### This section contains all subclasses of Shield



#################################################################################
######### This section contains all subclasses of Hammer

class Hammer(Weapon):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        self.abilities = ['Demolish','Starggering Strike','Imbued Strike']

class Mallet(Hammer):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.name = name
        self.damage = damage
        self.abilities = ['Demolish','Staggering Strike','Imbued Strike']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Hammerquake":"Bring down your weapon with enough force to cause tremors through the earth.",
    "Sudden Impact":"Deliver a swift blow to your target.",
    "Crash Down":"Leap into the air, brining your weapon down onto your target. With greater STR, you leap higher and do more damage."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Hammerquake":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Sudden Impact":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Crash Down":
            dmg = random.randint(1,6)

            if player_character.attributes['Strength'] > 20:
                dmg = dmg + 12
            elif 17 <= player_character.attributes['Strength'] < 20:
                dmg = dmg + 9
            elif 14 <= player_character.attributes['Strength'] < 17:
                dmg = dmg + 6
            else:
                dmg += 3
            print(f"You descend on your target, dealing {dmg} points of damage.")
            return player_health, dmg
        
    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Demolish
            dmg = random.randint(1,7)
            return dmg 

        elif ability_choice == 'b': ## b = Staggering Blow
            dmg = random.randint(1,7)
            return dmg

        elif ability_choice == 'c': ## c = Imbued Strike
            dmg = random.randint(1,7)
            return dmg

        else:
            return 0

class Mace(Hammer):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Demolish','Starggering Strike','Imbued Strike']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Shieldbreaker":"Attempt to break your enemy's defenses with a forceful swing.",
    "Skullcrusher":"Smash your target with enough force to stun them. This attack has a chance of dazing your opponent.",
    "Needlepoint":"Strike where your opponent is weakest, causing your target bleed over time.",
    "Shatter":"Appeal to the Heavens to demolish your enemy's defense, dealing large daamge even if their defenses stand."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Shieldbreaker":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Skullcrusher":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Needlepoint":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Shatter":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Demolish
            dmg = random.randint(1,8)
            return dmg 

        elif ability_choice == 'b': ## b = Staggering Blow
            dmg = random.randint(1,8)
            return dmg

        elif ability_choice == 'c': ## c = Imbued Strike
            dmg = random.randint(1,8)
            return dmg

        else:
            return 0

class Morningstar(Hammer):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Demolish','Starggering Strike','Imbued Strike']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Flamestrike":"Summon the fury of the Underworld, causing your weapon to burn with hellfire as you strike your foe",
    "Hellish Devastation":"Channel the wrath of the Underworld and use your weapon as a conduit to fire an energy blast",
    "Call of the Underworld":"Evoke the spirits of the abyss, causing an eruption of dark fire to engulf your foe ",
    "Infernal Rising":"Smash your weapon into the ground, causing the earth to splinter and hellfire to erupt upwards, burning your enemy "
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Flamestrike":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Hellish Devastation":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Call of the Underworld":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

        if ability_option == "Infernal Rising":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Demolish
            dmg = random.randint(1,9)
            return dmg 

        elif ability_choice == 'b': ## b = Staggering Blow
            dmg = random.randint(1,9)
            return dmg

        elif ability_choice == 'c': ## c = Imbued Strike
            dmg = random.randint(1,9)
            return dmg

        else:
            return 0

class Maul(Hammer):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Demolish','Starggering Strike','Imbued Strike']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Earthshaker":"Leap at your target, bring your weapon down with enough force to cause lasting tremors in the earth below",
    "Wild Devestation":"Become a conduit of Fury an attack your target with relentless pursuit",
    "Blunt Force Trauma":"Crush your target with overwhelming strength",
    "Cyclonic Rift":"Swing your weapon with such force that a vortex opens to damage your foe"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Earthshaker":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Wild Devestation":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Blunt Force Trauma":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Cyclonic Rift":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Demolish
            dmg = random.randint(1,10)
            return dmg 

        elif ability_choice == 'b': ## b = Staggering Blow
            dmg = random.randint(1,10)
            return dmg

        elif ability_choice == 'c': ## c = Imbued Strike
            dmg = random.randint(1,10)
            return dmg

        else:
            return 0

class Warhammer(Hammer):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ['Demolish','Starggering Strike','Imbued Strike']
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Mjolnir's Call":"Throw your weapon at your target, dealing immediate bludgeoning damage. Upon connecting, call upon the God of Thunder and strike your opponent with a bolt of lightning. ",
    "Titan's Fury":"Become a conduit for the Old Gods, growing to Titan size for a short duration. Your attacks are empowered and you rapidly heal.",
    "Call of the Forge God":"Summon a Molten Ram to charge your target, damaging and knocking them down."
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Mjolnir's Call":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Avalanche Slam":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Titan's Fury":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Call of the Forge God":
            dmg = random.randint(1,6)

            if player_character.attributes['Intelligence'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Demolish
            dmg = random.randint(1,11)
            return dmg 

        elif ability_choice == 'b': ## b = Staggering Blow
            dmg = random.randint(1,11)
            return dmg

        elif ability_choice == 'c': ## c = Imbued Strike
            dmg = random.randint(1,11)
            return dmg

        else:
            return 0

#################################################################################
######### This section contains all subclasses of Bow

class Bow(Weapon):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        self.abilities = ["Focused Shot","Swift Shot","Crossfire"]
    
class Shortbow(Bow):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Focused Shot","Swift Shot","Crossfire"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Arcane Arrow":"Focus and infuse your need arrow with arcane energy",
    "Power Shot":"Draw your bow to the limit and fire a high-velocity arrow",
    "Piercing Arrow":"Fire a arrow that pierces your target's defenses"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Arcane Arrow":
            dmg = random.randint(1,6)

            if player_character.attributes['Wisdow'] > 16:
                dmg += 3
            else:
                dmg += 1
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Power Shot":
            dmg = random.randint(2,10)

            if player_character.attributes['Dexterity'] > 16:
                dmg += 3
            else:
                dmg += 1
            print(f"You strike for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Piercing Arrow":
            dmg = random.randint(1,9)

            if player_character.attributes['Dexterity'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        if ability_choice  == 'a': ## a = Focused Shot
            dmg = random.randint(1,7)
            return dmg 

        elif ability_choice == 'b': ## b = Swift Shot
            dmg = random.randint(1,7)
            return dmg

        elif ability_choice == 'c': ## c = Crossfire
            dmg = random.randint(1,7)
            return dmg

        else:
            return 0

class Longbow(Bow):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Focused Shot","Swift Shot","Crossfire"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Serpent Strike":"Your next arrow strikes with a potent poison",
    "Radiant Arrow":"Fire an arrow imbued with sunlight, burning your target",
    "Crystal Volley":"Fire a flurry of crystal tipped arrows"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Serpent Strike":
            dmg = random.randint(1,6)

            if player_character.attributes['Wisdom'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Radiant Arrow":
            dmg = random.randint(1,6)

            if player_character.attributes['Wisdom'] > 16:
                dmg = dmg + 1
            else:
                dmg += 0
            print(f"The Sword hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Crystal Volley":
            dmg1 = random.randint(2,7)
            dmg2 = random.randint(2,7)
            dmg3 = random.randint(2,7)
            dmg = dmg1 + dmg2 + dmg3

            if player_character.attributes['Dexterity'] > 16:
                dmg += 2
            else:
                dmg += 0
            print(f"Your first arrows deals {dmg1} points of damage.")
            print(f"You second deals {dmg2} points of damage.")
            print(f"You final arrow hits for {dmg3} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Shot
            dmg = random.randint(1,8)
            return dmg 

        elif ability_choice == 'b': ## b = Swift Shot
            dmg = random.randint(1,8)
            return dmg

        elif ability_choice == 'c': ## c = Crossfire
            dmg = random.randint(1,8)
            return dmg

        else:
            return 0

class Composite_Bow(Bow):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Focused Shot","Swift Shot","Crossfire"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Flame Volley":"Fire a volley of fire-tipped arrows, burning your target",
    "Spectral Shot":"Fire an arrow infused with ethereal energy that moves through the Aether to your target",
    "Tempest's Rage":"Fire an arrow into the sky, infusing it with elemntal energy, and calling it to strike your target"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Flame Volley":
            dmg1 = random.randint(3,8)
            dmg2 = random.randint(2,9)
            dmg3 = random.randint(4,6)
            dmg = dmg1 + dmg2 + dmg3

            if player_character.attributes['Dexterity'] > 16:
                dmg += 5
            else:
                dmg += 0
            print(f"Your first arrows deals {dmg1} points of damage.")
            print(f"You second deals {dmg2} points of damage.")
            print(f"You final arrow hits for {dmg3} points of damage.")
            return player_health, dmg
        
        if ability_option == "Spectral Shot":
            dmg = random.randint(5,19)

            if player_character.attributes['Wisdom'] > 16:
                dmg +=5
            else:
                dmg += 0
            print(f"You arrow strikes for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Tempest's Rage":
            dmg = random.randint(6,18)

            if player_character.attributes['Dexterity'] > 16:
                dmg += 5
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Shot
            dmg = random.randint(1,9)
            return dmg 

        elif ability_choice == 'b': ## b = Swift Shot
            dmg = random.randint(1,9)
            return dmg

        elif ability_choice == 'c': ## c = Crossfire
            dmg = random.randint(1,9)
            return dmg

        else:
            return 0

class Recurve_Bow(Bow):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Focused Shot","Swift Shot","Crossfire"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Snipe":"A focused, aimed shot that strikes your target precisely at its weak point for greater damage",
    "Voidstar Arrows":"Infuse a set of arrows with voidborne energy",
    "Bloodhunt":"Mark your target and fire a pair of arrows that heal you for a portion of the damage done"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        
        if ability_option == "Snipe":
            dmg = random.randint(5,25)

            if player_character.attributes['Dexterity'] > 16:
                dmg += 5
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Voidstar Arrows":
            dmg1 = random.randint(1,11)
            dmg2 = random.randint(5,9)
            dmg3 = random.randint(2,13)
            dmg = dmg1 + dmg2 + dmg3

            if player_character.attributes['Dexterity'] > 16:
                dmg += 2
            else:
                dmg += 0
            print(f"Your first arrows deals {dmg1} points of damage.")
            print(f"You second deals {dmg2} points of damage.")
            print(f"You final arrow hits for {dmg3} points of damage.")
            return player_health, dmg
        
        if ability_option == "Bloodhunt":
            dmg1 = random.randint(3,11)
            dmg2 = random.randint(2,15)
            dmg = dmg1 + dmg2
            heal = dmg // 2
            player_health += heal

            if player_character.attributes['Wisdom'] > 16:
                dmg += 4
            else:
                dmg += 0
            print(f"Your first arrows deals {dmg1} points of damage.")
            print(f"You second deals {dmg2} points of damage.")
            print(f"Your Bloodhunt heals you for {heal}")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Shot
            dmg = random.randint(1,10)
            return dmg 

        elif ability_choice == 'b': ## b = Swift Shot
            dmg = random.randint(1,10)
            return dmg

        elif ability_choice == 'c': ## c = Crossfire
            dmg = random.randint(1,10)
            return dmg

        else:
            return 0

class Aetherbow(Bow):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Focused Shot","Swift Shot","Crossfire"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Solar Flare":"Call upon the power of the sun, drawing and firing an arrow of pure starfire",
    "Silvermoon":"Appeal to the Night, drawing and firintg an arrow of pure moonlight",
    "Verdance":"Call upon the Briar to grow around you and regenerate your life force",
    "True Shot":"Fire an ethereal arrow straight through your target. This ability has a chance to instantly kill its target"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Solar Flare":
            dmg = random.randint(7,19)

            if player_character.attributes['Wisdom'] > 16:
                dmg += 5
            else:
                dmg += 0
            print(f"Your solar-tipped arrow strikes for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Silvermoon":
            dmg = random.randint(7,19)

            if player_character.attributes['Wisdom'] > 16:
                dmg += 5
            else:
                dmg += 0
            print(f"You moon-tipped arrow hits for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Verdance":
            dmg = 0
            heal = random.randint(10,25)
            if player_character.attributes['Wisdom'] > 16:
                heal += 5
            else:
                heal += 0
            player_health += heal    
            print(f"You deal no damage, but you heal for {heal}. You now have {player_health} hit points.")
            return player_health, dmg
        
        if ability_option == "True Shot":
            dmg = random.randint(1,25)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("Your arrow pierces your target and kills it instantly.")
            elif kill < 19:
                if player_character.attributes['Dexterity'] > 16:
                    dmg += 8
                elif 10 <= player_character.attributes['Dexterity'] <= 16:
                    dmg += 5
                else:
                    dmg += 0 
                print(f"Your arrow deals {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Focused Shot
            dmg = random.randint(1,11)
            return dmg 

        elif ability_choice == 'b': ## b = Swift Shot
            dmg = random.randint(1,11)
            return dmg

        elif ability_choice == 'c': ## c = Crossfire
            dmg = random.randint(1,1)
            return dmg

        else:
            return 0

#################################################################################
######### This section contains all subclasses of Daggers

class Dagger(Weapon):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        self.abilities = ["Kidney Shot","Go For The Throat","Quickstrike"]

class Dirk(Dagger):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Kidney Shot","Go For The Throat","Quickstrike"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Veiled Strike":"Sprint at your foe, concealing your blade until the last moment to strike",
    "Feint":"Fade away from your target, reappearing to its rear and striking it from behind",
    "Shadowstrike":"Leap through the shadows and strike your target"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Veiled Strike":
            dmg = random.randint(2,8)

            if player_character.attributes['Dexterity'] > 16:
                dmg += 4
            elif 12 <= player_character.attributes['Dexterity'] <= 16:
                dmg += 3    
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Feint":
            dmg = random.randint(2,6)

            if player_character.attributes['Dexterity'] > 14:
                dmg += 3
            else:
                dmg += 0
            print(f"You strike for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Shadowstrike":
            dmg = random.randint(1,10)

            if player_character.attributes['Dexterity'] > 15:
                dmg += 4
            elif 11 <= player_character.attributes['Dexterity'] <= 15:
                dmg += 3    
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Kidney Shot
            dmg = random.randint(1,7)
            return dmg 

        elif ability_choice == 'b': ## b = Go For The Throat
            dmg = random.randint(1,7)
            return dmg

        elif ability_choice == 'c': ## c = Quickstrike
            dmg = random.randint(1,7)
            return dmg

        else:
            return 0

class Kris(Dagger):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Kidney Shot","Go For The Throat","Quickstrike"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Mounting Dread":"Channel Underworld energy to sap your target of lifeforce",
    "Mirage":"Cause an illusory image of yourself to distract your target as you dash to strike",
    "Shadowstep":"Seamlessly teleport through the darkness to your target and strike at a weak point"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Mounting Dread":
            dmg = random.randint(4,9)

            if player_character.attributes['Wisdom'] > 16:
                dmg += 5
            if 13 <= player_character.attributes['Wisdom'] <= 16:
                dmg += 3
            else:
                dmg += 0
            print(f"You sap your target of {dmg} hit points.")
            return player_health, dmg
        
        if ability_option == "Mirage":
            dmg = random.randint(4,12)

            if player_character.attributes['Intelligence'] >= 15:
                dmg += 5
            else:
                dmg += 0
            print(f"You hit for {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Shadowstep":
            dmg = random.randint(3,9)

            if player_character.attributes['Dexterity'] > 16:
                dmg += 4
            if 12 <= player_character.attributes['Dexterity'] <= 16:
                dmg += 2
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Kidney Shot
            dmg = random.randint(1,9)
            return dmg 

        elif ability_choice == 'b': ## b = Go For The Throat
            dmg = random.randint(1,9)
            return dmg

        elif ability_choice == 'c': ## c = Quickstrike
            dmg = random.randint(1,9)
            return dmg

        else:
            return 0

class Sai(Dagger):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Kidney Shot","Go For The Throat","Quickstrike"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Venom's Sting":"Stab your target with a blade coated in harsh poison",
    "Aether Stab":"Throw your blade out of this place, forcing it to re-enter and stirke your foe",
    "Corruption":"Call upon the Void to take hold of your target, draining its lifeforce",
    "Malevolence":"Call upon the shadows to stab at your target, piercing its soul"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Venom's Sting":
            dmg = random.randint(5,15)

            if (player_character.attributes['Dexterity'] > 15) or (player_character.attributes['Wisdom'] > 15):
                dmg += 6
            elif (10 <= player_character.attributes['Dexterity'] >= 14) or (10 <= player_character.attributes['Wisdom'] >= 14):
                dmg += 4
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Aether Stab":
            dmg = random.randint(4,18)

            if player_character.attributes['Dexterity'] > 15:
                dmg += 6
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Corruption":
            dmg = random.randint(6,15)

            if player_character.attributes['Wisdom'] > 16:
                dmg += 4
            else:
                dmg += 0
            print(f"You drain your target for {dmg} hit points.")
            return player_health, dmg
        
        if ability_option == "Malevolence":
            dmg = random.randint(8,15)

            if player_character.attributes['Wisdom'] > 16:
                dmg += 4
            if 12 <= player_character.attributes['Wisdom'] <= 16:
                dmg += 3
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Kidney Shot
            dmg = random.randint(1,10)
            return dmg 

        elif ability_choice == 'b': ## b = Go For The Throat
            dmg = random.randint(1,10)
            return dmg

        elif ability_choice == 'c': ## c = Quickstrike
            dmg = random.randint(1,10)
            return dmg

        else:
            return 0

class Serpant_Blades(Dagger):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.abilities = ["Kidney Shot","Go For The Throat","Quickstrike"]
        self.special_ability, self.special_ability_description = self._special_ability()
        text = f"""
{self.name} has a damage class of {self.damage}
{self.name}'s special ability:
{self.special_ability}: {self.special_ability_description}"""
        for character in text:
            if character == ' ':
                time.sleep(.05)
            print (character,end='',flush=True)
            time.sleep(.05)
        print('\n')

    def get_special_ability(self):
        return self.special_ability, self.special_ability_description

    def _special_ability(self):
        ability_options = {
    "Nightmare":"Vanish and appear as a nightmare in your target's mind to strike their consciousness",
    "Death Lotus":"Spin rapidly in place, throwing knives is all directions and slicing targets near by",
    "Whispers of Ruin":"Appeal to the Underworld to take a hold in your target's mind. This ability has a chance of instantly killing your foe",
    "Path of Exile":"Channel through your weapon and piece your target's lifeforce. This ability has a chance of ripping your target's soul from its body and killing it instantly"
    }
        
        ability_option = random.choice(list(ability_options.keys()))
        return ability_option, ability_options[ability_option]

    def special_ability_actions(self, player_character, player_health):
        ability_option = self.special_ability
        if ability_option == "Nightmare":
            dmg = random.randint(8,16)

            if player_character.attributes['Wisdom'] > 16:
                dmg += 5
            if 12 <= player_character.attributes['Wisdom'] <= 16:
                dmg += 4
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Death Lotus":
            dmg1 = random.randint(2,7)
            dmg2 = random.randint(1,6)
            dmg3 = random.randint(2,8)
            dmg4 = random.randint(1,5)
            dmg = dmg1 + dmg2 + dmg3 + dmg4

            if player_character.attributes['Dexterity'] > 16:
                dmg += 5
            elif 12 <= player_character.attributes['Dexterity'] <= 16:
                dmg += 3
            else:
                dmg += 0
            print(f"You deal {dmg} points of damage.")
            return player_health, dmg
        
        if ability_option == "Whispers of Ruin":
            dmg = random.randint(9,25)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("Visions of death overwhelm your foe. You see life fade from its eyes.")
            elif kill < 19:
                if player_character.attributes['Wisdom'] > 16:
                    dmg = dmg + 8
                elif 10 <= player_character.attributes['Wisdom'] <= 16:
                    dmg = dmg + 6
                else:
                    dmg += 0 
            return player_health, dmg
        
        if ability_option == "Path of Exile":
            dmg = random.randint(9,25)
            kill = random.randint(1,20)

            if kill >= 19:
                dmg = 100000000
                print("Your blade removes your target's soul from this plane.")
            elif kill < 19:
                if player_character.attributes['Wisdom'] > 16:
                    dmg = dmg + 8
                elif 10 <= player_character.attributes['Wisdom'] <= 16:
                    dmg = dmg + 6
                else:
                    dmg += 0 
            return player_health, dmg

    def melee_dmg(self,ability_choice):
        ability_choice = ability_choice
        if ability_choice  == 'a': ## a = Kidney Shot
            dmg = random.randint(1,11)
            return dmg 

        elif ability_choice == 'b': ## b = Go For The Throat
            dmg = random.randint(1,11)
            return dmg

        elif ability_choice == 'c': ## c = Quickstrike
            dmg = random.randint(1,11)
            return dmg

        else:
            return 0

