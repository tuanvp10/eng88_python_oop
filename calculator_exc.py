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

