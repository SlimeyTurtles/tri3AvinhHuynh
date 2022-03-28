class Factorial:
    def __init__(self):
        self.output = 1

    def __call__(self, n):
        for num in range(n):
            self.output = self.output * (num + 1)
        return self.output


Fact = Factorial()

if __name__ == "__main__":
    print("Factorial Class")

    input = 5

    print("input: " + str(input))
    print(Fact(int(input)))
