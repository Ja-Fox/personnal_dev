from Archmage_Class import Archmage
from Assassin_Class import Assassin
from Lionheart_Class import Lionheart
from Paladin_Class import Paladin
from SpellShot_Class import Spell_Shot
from Ritualist_Class import Ritualist
import Weapon_Classes
import Loot_Items
import random

def weapon_generator():
        weapon_drop_options = ["Novice Staff", "Adept Staff", "Journeyman Staff","Archmage Staff","Ritualist Staff","Dirk","Kris", "Sai","Serpant Blades"
                                "Gladius", "Sabre", "Longsword","Broadsword","Greatsword","Mallet", "Mace", "Morningstar","Maul","Warhammer","Shortbow",
                                "Longbow", "Composite Bow","Recurve Bow","Aetherbow",]
        weapon_name_options = ["Brightmoon","Supernova","Spelltheif","Overclock","Mercy","Fury","Reckoning","Silence","Discord"]
        weapon_damage_options = [1,2,3,4,5]
        weapon_drop = random.choice(weapon_drop_options)
        weapon_name = random.choice(weapon_name_options)
        weapon_damage = random.choice(weapon_damage_options)

        ## Staff Drop options ##
        if weapon_drop == "Novice Staff":
                weapon = Weapon_Classes.Novice_Staff(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Adept Staff":
                weapon = Weapon_Classes.Adept_Staff(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Journeyman Staff":
                weapon = Weapon_Classes.Journeyman_Staff(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Archmage Staff":
                weapon = Weapon_Classes.Archmage_Staff(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Ritualist Staff":
                weapon = Weapon_Classes.Ritualist_Staff(weapon_name,weapon_damage)
                return weapon
        ## Sword Drop options ##
        if weapon_drop == "Gladius":
                weapon = Weapon_Classes.Gladius(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Sabre":
                weapon = Weapon_Classes.Sabre(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Longsword":
                weapon = Weapon_Classes.Longsword(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Broadsword":
                weapon = Weapon_Classes.Broadsword(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Greatsword":
                weapon = Weapon_Classes.Greatsword(weapon_name,weapon_damage)
                return weapon
        ## Mace Drop options ##
        if weapon_drop == "Mallet":
                weapon = Weapon_Classes.Mallet(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Mace":
                weapon = Weapon_Classes.Mace(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Morningstar":
                weapon = Weapon_Classes.Morningstar(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Maul":
                weapon = Weapon_Classes.Maul(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Warhammer":
                weapon = Weapon_Classes.Warhammer(weapon_name,weapon_damage)
                return weapon
        ## Dagger Drop options ##
        if weapon_drop == "Dirk":
                weapon = Weapon_Classes.Dirk(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Sai":
                weapon = Weapon_Classes.Sai(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Kris":
                weapon = Weapon_Classes.Kris(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Serpant Blades":
                weapon = Weapon_Classes.Serpant_Blades(weapon_name,weapon_damage)
                return weapon
        ## Bow Drop options ##
        if weapon_drop == "Shortbow":
                weapon = Weapon_Classes.Shortbow(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Longbow":
                weapon = Weapon_Classes.Longbow(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Composite Bow":
                weapon = Weapon_Classes.Composite_Bow(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Recurve Bow":
                weapon = Weapon_Classes.Recurve_Bow(weapon_name,weapon_damage)
                return weapon
        if weapon_drop == "Aetherbow":
                weapon = Weapon_Classes.Aetherbow(weapon_name,weapon_damage)
                return weapon

def dependent_weapon_gen(player_character):
        if isinstance(player_character,Archmage):
                weapon_drop_options = ["Novice Staff", "Adept Staff", "Journeyman Staff","Archmage Staff","Ritualist Staff"]
                weapon_name_options = ["Brightmoon Staff","Shadowcaster","Spelltheif's Edge","Blightwood Staff","Frostwood Staff","Silence","Rod of Discord","Tempest Staff","Voidstar","Seraphim","Magebane"]
                weapon_drop = random.choice(weapon_drop_options)
                weapon_name = random.choice(weapon_name_options)

                if weapon_drop == "Novice Staff":
                        weapon = Weapon_Classes.Novice_Staff(weapon_name,1)
                        return weapon
                if weapon_drop == "Adept Staff":
                        weapon = Weapon_Classes.Adept_Staff(weapon_name,2)
                        return weapon
                if weapon_drop == "Journeyman Staff":
                        weapon = Weapon_Classes.Journeyman_Staff(weapon_name,3)
                        return weapon
                if weapon_drop == "Archmage Staff":
                        weapon = Weapon_Classes.Archmage_Staff(weapon_name,4)
                        return weapon
                if weapon_drop == "Ritualist Staff":
                        weapon = Weapon_Classes.Ritualist_Staff(weapon_name,5)
                        return weapon

        if isinstance(player_character,Assassin):
                weapon_drop_options = ["Novice Staff", "Adept Staff", "Journeyman Staff","Archmage Staff","Ritualist Staff"]
                weapon_name_options = ["Viperfang","Ghostwalker","Last Whisper","Serpent's Kiss","Undertow","Ebony Shiv","Duskfire","Nightshade","Bloodthorn"]
                weapon_drop = random.choice(weapon_drop_options)
                weapon_name = random.choice(weapon_name_options)

                if weapon_drop == "Dirk":
                        weapon = Weapon_Classes.Dirk(weapon_name,1)
                        return weapon
                if weapon_drop == "Sai":
                        weapon = Weapon_Classes.Sai(weapon_name,2)
                        return weapon
                if weapon_drop == "Kris":
                        weapon = Weapon_Classes.Kris(weapon_name,3)
                        return weapon
                if weapon_drop == "Serpant Blades":
                        weapon = Weapon_Classes.Serpant_Blades(weapon_name,4)
                        return weapon

        if isinstance(player_character,Lionheart):
                weapon_drop_options = ["Gladius", "Sabre", "Longsword","Broadsword","Greatsword"]
                weapon_name_options = ["Frostbite","Fury","Reckoning","Soulreaver","Obsidian Edge","Dawn","Dusk","Seraph's Keyblade","Vengence"]
                weapon_drop = random.choice(weapon_drop_options)
                weapon_name = random.choice(weapon_name_options)

                if weapon_drop == "Gladius":
                        weapon = Weapon_Classes.Gladius(weapon_name,1)
                        return weapon
                if weapon_drop == "Sabre":
                        weapon = Weapon_Classes.Sabre(weapon_name,2)
                        return weapon
                if weapon_drop == "Longsword":
                        weapon = Weapon_Classes.Longsword(weapon_name,3)
                        return weapon
                if weapon_drop == "Broadsword":
                        weapon = Weapon_Classes.Broadsword(weapon_name,4)
                        return weapon
                if weapon_drop == "Greatsword":
                        weapon = Weapon_Classes.Greatsword(weapon_name,5)
                        return weapon

        if isinstance(player_character,Paladin):
                weapon_drop_options = ["Mallet", "Mace", "Morningstar","Maul","Warhammer"]
                weapon_name_options = ["Endgame","Thunderclap","Ironheart","Arcana","Skullcrusher","Earthshaker","Basilisk's Bane","Morningstar","Griffenclaw"]
                weapon_drop = random.choice(weapon_drop_options)
                weapon_name = random.choice(weapon_name_options)

                if weapon_drop == "Mallet":
                        weapon = Weapon_Classes.Mallet(weapon_name,1)
                        return weapon
                if weapon_drop == "Mace":
                        weapon = Weapon_Classes.Mace(weapon_name,2)
                        return weapon
                if weapon_drop == "Morningstar":
                        weapon = Weapon_Classes.Morningstar(weapon_name,3)
                        return weapon
                if weapon_drop == "Maul":
                        weapon = Weapon_Classes.Maul(weapon_name,4)
                        return weapon
                if weapon_drop == "Warhammer":
                        weapon = Weapon_Classes.Warhammer(weapon_name,5)
                        return weapon

        if isinstance(player_character,Spell_Shot):
                weapon_drop_options = ["Shortbow", "Longbow", "Composite Bow","Recurve Bow","Aetherbow"]
                weapon_name_options = ["Swiftwind","Thornwood","Tailwind","Moonshadow","Warbow","Stormcaller","Venomstrike","Starfall","Talon","Eaglemark"]
                weapon_drop = random.choice(weapon_drop_options)
                weapon_name = random.choice(weapon_name_options)

                if weapon_drop == "Shortbow":
                        weapon = Weapon_Classes.Shortbow(weapon_name,1)
                        return weapon
                if weapon_drop == "Longbow":
                        weapon = Weapon_Classes.Longbow(weapon_name,2)
                        return weapon
                if weapon_drop == "Composite Bow":
                        weapon = Weapon_Classes.Composite_Bow(weapon_name,3)
                        return weapon
                if weapon_drop == "Recurve Bow":
                        weapon = Weapon_Classes.Recurve_Bow(weapon_name,4)
                        return weapon
                if weapon_drop == "Aetherbow":
                        weapon = Weapon_Classes.Aetherbow(weapon_name,5)
                        return weapon

        if isinstance(player_character,Ritualist):
                weapon_drop_options = ["Novice Staff", "Adept Staff", "Journeyman Staff","Archmage Staff","Ritualist Staff"]
                weapon_name_options = ["Brightmoon","Shadowcaster","Spelltheif's Edge","Blightwood Staff","Fury","Reckoning","Silence","Rod of Discord","Tempest","Voidstar","Seraphim","Magebane"]
                weapon_drop = random.choice(weapon_drop_options)
                weapon_name = random.choice(weapon_name_options)

                if weapon_drop == "Novice Staff":
                        weapon = Weapon_Classes.Novice_Staff(weapon_name,1)
                        return weapon
                if weapon_drop == "Adept Staff":
                        weapon = Weapon_Classes.Adept_Staff(weapon_name,2)
                        return weapon
                if weapon_drop == "Journeyman Staff":
                        weapon = Weapon_Classes.Journeyman_Staff(weapon_name,3)
                        return weapon
                if weapon_drop == "Archmage Staff":
                        weapon = Weapon_Classes.Archmage_Staff(weapon_name,5)
                        return weapon
                if weapon_drop == "Ritualist Staff":
                        weapon = Weapon_Classes.Ritualist_Staff(weapon_name,5)
                        return weapon

def potion_generator():
## Randomly choose which potion drops ##
    roll = random.randint(1,20)
    if roll >= 19:
        dropped_potion = Loot_Items.Life_Potion()
        return dropped_potion
    elif 15 <= roll < 19:
        dropped_potion = Loot_Items.Greater_Health_Potion()
        return dropped_potion
    elif 7 <= roll < 14:
        dropped_potion = Loot_Items.Health_Potion()
        return dropped_potion
    else:
        dropped_potion = Loot_Items.Minor_Health_Potion()
        return dropped_potion