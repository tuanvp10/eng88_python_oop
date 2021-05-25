# Creating a python snake class

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yum yum yum!"

    def climb(self):
        return "up we go! "

    def shed(self):
        return "Time to grow out of myself ! "


# dog_object = Python()
# print(dog_object.eyes)
# print(dog_object.eat())

python_object = Python()
print("This function is from Python class" + python_object.climb())
print("This function is from Snake class" + python_object.use_tongue_to_smell())


