height = 20

def tree(height):
    for i in range(height):
        for j in range(height-i):
            print("  ", end="")
        for j in range(i):
            print("  * ", end="")
        print()
    for i in range(round(height/4)):
        for j in range(height-1):
            print("  ", end="")
        print(" | |")

if __name__ == "__main__":
    print("Tree Function")
    print("Height: " + str(height))
    tree(height)