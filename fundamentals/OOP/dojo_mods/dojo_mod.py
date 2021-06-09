#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
from pets_mod import AngryCat, Pet
from ninjas_mod import Ninja

from ninjas_mod import Ninja
from pets_mod import Pet, AngryCat

pet_1 = Pet("Norma", "kitty", "sleeps", health=50, energy=50)
pet_2 = AngryCat("Doug", "assasin", "mauling", health=50, energy=50)

ninja_1 = Ninja("Karl", "mice", "salad", pet_1)
ninja_1.feed().walk()

ninja_2 = Ninja("Milquetoast", "old gum", "sandwiches", pet_2)

print(pet_2.name)
pet_2.noise()
print(pet_2.__dict__)
