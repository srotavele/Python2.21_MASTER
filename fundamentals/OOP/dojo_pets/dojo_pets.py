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

class Pet:
    def __init__(self, name, types, tricks, health = 50, energy = 50):
        self.name = name
        self.type = types
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 20
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Meow, hisssss!!!")

    def display_health(self):
        print(self.name, "Health =", self.health)

    def display_energy(self):
        print(self.name, "Energy =", self.energy)

pet_1 = Pet("Norma","Kitty","purrs")
print(pet_1.name)

ninja_1 = Ninja("Radar Bob","mice","salad",pet_1)
print(ninja_1.name)

ninja_1.walk().feed().bathe()
pet_1.eat().play().sleep().display_energy().display_health()
