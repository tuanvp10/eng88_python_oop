# Create animal class via animal file

class Animal:

    def __init__(self): # self refers to this class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "Nom nom nom nom!"

    def move(self):
        return "Moving all around the world"

# Create a object of our Animal class
# cat = Animal() # Creating a object of our Animal class = cat
# print(cat.breath()) # Breathing for cat is abstracted