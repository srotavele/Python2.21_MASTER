#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
class Ninja:
    def __init__(self, name, treats, pet_food, pet):
        self.name = name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"{self.name} is taking {pet_1.name} for a walk ")
        return self

    def feed(self):
        self.pet.eat()
        print(f"{self.name} is feeding {pet_1.name} dinner")
        return self

    def bathe (self):
        self.pet.noise()
        print(f"{self.name} is giving {pet_1.name} a bath")