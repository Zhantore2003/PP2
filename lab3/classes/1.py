class MyClass():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ") #Get a string from console input.

    def printReverse(self):
        print(self.reversed())

a = MyClass()

# Call the getString method
a.getString()

# Call the printString method
a.printReverse()

