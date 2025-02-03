########################
#### Health Potions ####

class Potion:
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal

class Minor_Health_Potion(Potion):
    def __init__(self, name = "Minor Health Potion", heal=5):
        super().__init__(name,heal)

class Health_Potion(Potion):
    def __init__(self, name='Health Potion', heal=10):
        super().__init__(name,heal)

class Greater_Health_Potion(Potion):
    def __init__(self, name='Greater Health Potion', heal=25):
        super().__init__(name,heal)
        
class Life_Potion(Potion):
    def __init__(self, name='Life Potion', heal=50):
        super().__init__(name,heal)

#########################
#### Inventory Items ####

