#Python OOP
## Packages
Packages and modules are pre-made blocks of code that can be used to perfor a particular task without the need to add your own code. They can be simply imported using the import command. It is also possible to import individual functions using the command from [package] import [function]. This has the advantage that the function can suimply be called by its name, rather than needing to specify the package name for every function call.

#### OS and SYS
These tow packages are useful for doing system-related tasks, such as getting the current working directory (an obvious use case for this would be contructing a filepath for saving or retrieving files).

#### Math - Sample code discussion
The `math` library contains a large amount of functions and values commonly used in mathematics. These are commonly used to perform operations such as rounding.

An example of this is shown here:
```python
import math

num1 = random()
print(num1)
if num1 >= 0.5:
    print(math.ceil(num1))
else:
    print(math.floor(num1))
```
#### Lambda
This type of function takes multiple arguments and returns a singular value. It has built-in functionality that helps us work out certain things

## Modules

## What are the four PILLARS of OOP
### - ABSTRACTION
Abstraction is the process of taking away characteristics to reduce something to an essential set of characteristics. User when modelling objects using classes and minimising the amount of information necessary for a user of a function to know in order to get usable software.
### - ENCAPSULATION
This means hiding data internal to a class from a client or external user. Use underscores to signal to other programmers that we do not want a variable changed. e.g. to indicate that var is private, we would define it as _var in our function.
DOB = 01/01/1990
### - INHERITANCE
This means that we can, and should, create "child classes", which take the properties of a "parent class" and "inherit" their traits as a starting point. For example, you might have a person class, but then have classes based on this such as worker, student, or similar.
### - POLYMORPHISM
This is the philosophy of having many forms available. This means you can overwrite methods from a parent class without changing the parent class. This means that if you had an employee class, you might write a different "pay" method depending on the way the employee was paid (e.g some are salaried, some hourly, some get bonuses, etc.)

## Example 
To demonstrate this, we create a quick class called Animal, containing a few typical features an animal might have:
```python
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
```
We can import this into another class, which we note as a child of the Animal class using the syntax `ChildClass(ParentClass)`. If we are writing in a separate file as we have done here, we also need to import the parent class we are basing our work on using, in this case, the command `from animal import Animal`. We can also inherit further, with "grandchild" classes, which we have done in the other files. Notice that we can call all the way up the inheritance tree, even being able to call Animal methods in the snake class even though it is the "great-grandchild" of that class.

Taking the example below, we see the great-grandchild of Animal, Python. An object of the python class can use methods from any of the predecessors, as the print statements show:

```python
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
```

```python
# Creating snake class as a child class from reptile class

from reptile import Reptile
class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        return "I can smell the taste of... "

snake_object = Snake()
# print("This function is from snake class " + snake_object.use_tongue_to_smell())
# print("This function is from reptile class " + snake_object.seek_heat())
# print("This function is from animal class " + snake_object.eat())
```
```python
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
```

## Example 2

This task is similar to the one done in Week 1, but to demonstrate the ability to inherit, it is split into two parts, a simple calculator (stored in oop_calc_exc.py), and a slightly more advanced calculator stored in functional_calc.

Starting with SimpleCalc:
```python
class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

calc_object = SimpleCalc()
print(calc_object.add(3, 3))
```
This contains four functions, for addition, subtraction, multiplication and division. If an object of SimpleCalc is instantiated, the functions can be accessed.

We now want to add more functionality to the calculator, in this case a check whether two numbers are divisible, a converter for inches to centimetres, and a function to calculate the area of a triangle.

To do this, we create a child class of SimpleCalc, which I have called FunctionalCalc:

```python
from oop_calc_exc import SimpleCalc

class FunctionalCalc(SimpleCalc):

    def __init__(self):
        super().__init__()

    def conversion(self, num1):
        return num1 * 2.54

    def divisible(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def triangle(self, height, width):
        return (height * width) / 2


fun_object = FunctionalCalc()

# Create a function for cm to inches

# Create a function for division_by 0, check if the number is divisible by 0, return True else return False

# Print statements for all the functions available in parent class as well as this child class
```
The final file will inherit from both SimpleCalc and FunctionalCalc

```python
from functional_calc import FunctionalCalc

class OopCalculator(FunctionalCalc):
    def __init__(self):
        super().__init__()

    def calculations(self):

            menu = int(input("Which from the menu, would you like to pick? ---> \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Convert cm to inches \n6. Area of a triangle \n7. Are the numbers divisible with no remainders \n---->"))
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter a number: "))
            calculate = True
            while calculate:
                if menu == 1:
                    print("Result: ", total.add(num1, num2))
                elif menu == 2:
                    print("Result: ", total.subtract(num1, num2))
                elif menu == 3:
                    print("Result: ", total.multiply(num1, num2))
                elif menu == 4:
                    print("Repeat: ", total.divide(num1, num2))
                elif menu == 5:
                    print("Repeat: ", total.conversion(num1, num2))
                elif menu == 6:
                    print("Repeat: ", total.triangle(num1, num2))
                elif menu == 7:
                    print("Repeat: ", total.divisible(num1, num2))
                break
total = OopCalculator()
total.calculations()
```
The functions we have added are available only in FunctionalCalc. However, the key thing is the below block of code:
```python
 def __init__(self):
        super().__init__()
```
using the `super().__init__()` statement means we are telling the interpreter to set up the initial conditions of our class in the same way as its parent class, or superclass. We can therefore access all of SimpleCalculator's functions, with the new functions being added on for our FunctionalCalculator class. This is what is known as inheritance, and a key aspect of OOP.






