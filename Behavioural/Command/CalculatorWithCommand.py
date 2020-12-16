class Calculator:
    def __init__(self, initial_value=0):
        self.__current_value = initial_value
        self.__history = []

    def executeCommand(self, command):
        self.__current_value = command.execute(self.__current_value)
        self.__history.append(command)

    def undo(self):
        self.__current_value = self.__history.pop().undo(self.__current_value)
    
    def show(self):
        print("Current Value =", self.__current_value)


class AddCommand:
    def __init__(self, num):
        self.__num = num

    def execute(self, current_value):
        return current_value+self.__num

    def undo(self, current_value):
        return current_value-self.__num


class SubstractCommand:
    def __init__(self, num):
        self.__num = num

    def execute(self, current_value):
        return current_value-self.__num

    def undo(self, current_value):
        return current_value+self.__num

if __name__ == "__main__":
    calc = Calculator()
    fns = {
        "a":lambda : calc.executeCommand(AddCommand(int(input("Enter Number to be added > ")))),
        "s":lambda : calc.executeCommand(SubstractCommand(int(input("Enter Number to be substracted > ")))),
        "u":calc.undo,
        "e":quit
    }
    while(True):
        calc.show()
        choice = input("Enter a to add, s to substract, u to undo, e to exit > ")
        fns.get(choice, quit)()
