# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class MyString():
    def __init__(self):
        str = ''

    def getString(self):
        print("Please provide the input:")
        self.str = input()
        return self.str

    def printString(self):
        print(self.str.upper())


myStrObj = MyString()
myStrObj.getString()
myStrObj.printString()

with open('L1Q1.py') as f:
    print(f.readline())