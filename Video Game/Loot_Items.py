########################
#### Health Potions ####

class Potion:
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal

class Minor_Health_Potion(Potion):
    def __init__(self, name = "Minor Health Potion", heal=5):
        super().__init__(name,heal)
        return heal

class Health_Potion(Potion):
    def __init__(self, name='Health Potion', heal=10):
        super().__init__(name,heal)
        return heal

class Greater_Health_Potion(Potion):
    def __init__(self, name='Greater Health Potion', heal=25):
        super().__init__(name,heal)
        return heal
        
class Life_Potion(Potion):
    def __init__(self, name='Life Potion', heal=50):
        super().__init__(name,heal)
        return heal

#########################
#### Inventory Items ####

class Item:
    def __init__(self, name):
        self.name = name

class Rope(Item):
    def __init__(self):
        super().__init__(name='Rope')

def list_potions_in_inventory(potion_inventory):
    for each_item in potion_inventory:
        print (each_item)


