import re

class palindrome:
    def __init__(self):
        self.index = 0
        self.input = ""
        self.cleanList = ["\s", "-", ",", "!", "?", "."]

    def clean(self):
        self.input = self.input.lower()
        for element in self.cleanList:
            self.input.replace(element, '')

    def __call__(self, input):
        self.input = input
        self.clean()
        print(self.input)


pal = palindrome()
pal("giraf-fe")
