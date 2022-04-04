import math

class Palindrome:
    def __init__(self):
        self.index = 0
        self.input = ""
        self.cleanList = [" ", "-", ",", "!", "?", "."]

    def clean(self):
        self.input = self.input.lower()
        for element in self.cleanList:
            self.input = self.input.replace(element, '')
        return self.input

    def __call__(self, input):
        self.input = input
        self.clean()

        index = math.floor(len(self.input)/2)
        palindrome = True

        for i in range(index):
            if self.input[i] != self.input[::-1][i]:
                print("Error on index: " + str(i), str((len(self.input) - i)))
                palindrome = False

        if palindrome == False:
            print("This is not a palindrome")
        else:
            print("This is a palindrome")


pal = Palindrome()
pal("")
