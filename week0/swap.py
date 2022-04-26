def swap(age1, age2):
    print("Old Numbers: " + str(age1), str(age2))
    if age1 > age2:
        temp = age2
        age2 = age1
        age1 = temp
    print("Swapped Numbers: " + str(age1), str(age2))

if __name__ == "__main__":
    print("Swap Function")
    num1 = 5
    num2 = 3
    swap(num1, num2)