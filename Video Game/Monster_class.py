import random

class Monster:

    def __init__(self):
        pass

    def get_easy_monster_encounter(self):
        encounter_options= ['Troll','Dredge','Kobold','Goblin','Wendigo','Bugbear',"Wraith","Direwolf","Harpy","Corrupted Treant"]
        self.monster = random.choice(encounter_options)
        return self.monster

    def get_easy_monster_health(self):
        self.monster_health = random.randint(5,12)
        return self.monster_health
    
    def medium_monster_encounter_options(self):
        encounter_options= ['Wendigo','Bugbear',]
        self.monster = random.choice(encounter_options)
        return self.monster

    def medium_easy_monster_health(self):
        self.monster_health = random.randint(10,25)
        return self.monster_health
    

class Boss_Monster:

    def __init__(self):
        pass

    def get_boss_monster_encounter(self):
        boss_options = ["Dreadmaw","Abyssal","Ragefire","Shreika","Banshee","Broodmother"]
        self.boss_monster = random.choice(boss_options)
        return self.boss_monster
    
    def get_boss_monster_health(self):
        self.monster_health = random.randint(30,45)
        return self.monster_health
