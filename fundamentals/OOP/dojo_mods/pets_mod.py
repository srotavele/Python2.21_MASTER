#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
class Pet:
    def __init__(self, name, types, tricks, health=50, energy=50):
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
        print("Meow")

    def display_health(self):
        print(self.name, "Health =", self.health)
        return self

    def display_energy(self):
        print(self.name, "Energy =", self.energy)
        return self


class AngryCat(Pet):
    def __init__(self, name, types, tricks, health=50, energy=50):
        super().__init__(name, types, tricks, health=50, energy=50)

    def noise(self):
        print("Hissssssssssss!!!!!")


class SleepyCat(AngryCat):
    def __init__(self, name, types, tricks, health=50, energy=50):
        super().__init__(name, types, tricks, health=50, energy=50)

    def sleep(self):
        self.health += 30
        self.energy += 30
        return self

    def noise(self):
        print("purrrrrr")
