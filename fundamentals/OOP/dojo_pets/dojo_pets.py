#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

class Ninja:
    def __init__(first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name, types, tricks, health = 0, energy = 0)
    
    def walk(self):
        pass
    
    def feed(self):
        pass
    
    def bathe (self):
        pass
    
    
ninja_1 = Ninja( "Radar", "Bob","caviar","Kibbles_n_Bits",)
print(ninja_1.name)
    
    
class Pet:
    def __init__(name, types, tricks, health = 0, energy = 0):
        self.name = name
        self.type = types
        self.tricks = tricks
    
    def sleep(self):
        self.energy +20
    
    def eat(self):
        self.health +10
        self.energy +5 
    
    def play(self):
        self.health  +5
    
    def noise(self):
        print("Meow, hisssss!!!")
        
pet_1 = Pet("Norma","kitty", "maul",)
print(pet_1.name)