# Creating a reptile class to inherit everything from Animal Class

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        # We have a keyword called SUPER which inherits everything from parent class at the time of the initialisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return "It is rainy and windy, where is the sun!? "

    def hunt(self):
        return "Hunting for food until you get it!"

    def use_venom(self):
        return "If I have got it, I am using it!"

reptile_object = Reptile()

# print("This function is from Reptile class" + reptile_object.hunt())
# print("This function is Inherited from Animal class " + reptile_object.eat())

# This is the amazing benefit of using OOP and Inheritance