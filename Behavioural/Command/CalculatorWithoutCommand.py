class Calculator:
    def __init__(self, initial_value=0):
        self.__current_value = initial_value

    def add(self, num):
        self.__current_value += num

    def substract(self, num):
        self.__current_value -= num

    def show(self):
        print("Current value =", self.__current_value)


calc = Calculator()
fns = {
    "a": lambda: calc.add(int(input("Enter Number to be added > "))),
    "s": lambda: calc.substract(int(input("Enter Number to be substracted > "))),
    "e": quit
}
while(True):
    calc.show()
    fns.get(input("Enter a to Add, s to substract, e to exit >"), quit)()
