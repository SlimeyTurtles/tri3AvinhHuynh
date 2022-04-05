class lcm:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.maximum = 0

    # Function to find the LCM of two Numbers
    def __call__(self, a, b):
        if a > b:
            maximum = a
        else:
            maximum = b
        while (True):
            if maximum % a == 0 and maximum % b == 0:
                break
            maximum = maximum + 1
        return maximum

def lcmClassDriver():
    leastCommonMultiplier = lcm()

    a = int(input(" Enter the First Value for LCM: "))
    b = int(input(" Enter the Second Value for LCM: "))
    output = leastCommonMultiplier(a, b)
    print("\n Least Common Multiple of {0} and {1} is: {2}".format(a, b, output))
    print()


