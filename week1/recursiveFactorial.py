def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)


if __name__ == "__main__":
    print("Recursive Factorial Function")
    num = 4
    print("The factorial of", num, "is", recur_factorial(num))
    num = 3
    print("The factorial of", num, "is", recur_factorial(num))
    num = 11
    print("The factorial of", num, "is", recur_factorial(num))