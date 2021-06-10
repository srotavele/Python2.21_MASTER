#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
from pets_mod import AngryCat, Pet
from ninjas_mod import Ninja

from ninjas_mod import Ninja
from pets_mod import Pet, AngryCat, SleepyCat

pet_1 = Pet("Norma", "kitty", "sleeps", health=50, energy=50)
pet_2 = AngryCat("Doug", "assasin", "mauling", health=50, energy=50)
pet_3 = SleepyCat("Lump", "couch potato", "yawning", health=50, energy=50)

ninja_1 = Ninja("Karl", "mice", "salad", pet_1)
ninja_1.feed().walk()

ninja_2 = Ninja("Milquetoast", "old gum", "sandwiches", pet_2)
ninja_2.walk().bathe()

ninja_3 = Ninja("Sven", "bacon", "hot pockets", pet_3)
ninja_3.feed().bathe()

pet_1.display_energy().display_health()
pet_2.display_energy().display_health()
pet_3.display_energy().display_health()
print(pet_1.__dict__)
print(pet_2.__dict__)
print(pet_3.__dict__)
print (pet_1)
