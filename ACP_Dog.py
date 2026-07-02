class Dog:
    animal = "Dog"
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and White")
print("Dog1 is a {}".format(dog1.animal))
print("Dog2 is a {}".format(dog2.animal))
print("Dog1 is a {} and its colour is {}".format(dog1.breed, dog1.colour))
print("Dog2 is a {} and its colour is {}".format(dog2.breed, dog2.colour))