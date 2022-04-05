class recursiveFibonacci():
    def __init__(self):
        self.num1 = 0
        self.num2 = 1
        self.i = 1

    def __call__(self, index):
        if self.i > index:
            return self.num2
        else:
            temp = self.num1 + self.num2
            print("index " + str(self.i) + ": " + str(self.num1) + " + " + str(self.num2) + " = " + str(temp))
            self.num1 = self.num2
            self.num2 = temp
            self.i += 1
            rec(index)

rec = recursiveFibonacci()

def recursiveFibonacciDriver():
    print("Recursive Fibonacci")
    index = 6
    print("Index: " + str(index))
    rec(index)

if __name__ == "__main__":
    recursiveFibonacciDriver()
