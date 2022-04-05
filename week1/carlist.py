# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Avinh",
    "LastName": "Huynh",
    "DOB": "December 27",
    "Residence": "Escondido",
    "Email": "avinhahuynh@gmail.com",
    "Shoes": ["puma", "sports crocs"]
})

InfoDb.append({
    "FirstName": "Aiden",
    "LastName": "Huynh",
    "DOB": "May 12",
    "Residence": "Escondido",
    "Email": "bubuhuynh@gmail.com",
    "Shoes": ["Black ones", "The other black ones","Sports crocs"]
})

InfoDb.append({
    "FirstName": "Alani",
    "LastName": "Huynh",
    "DOB": "May 4",
    "Residence": "Escondido",
    "Email": "alaninhuynh@gmail.com",
    "Shoes": ["Way too many"]
})


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Shoes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Shoes"]))  # join allows printing a string list with separator
    print()


# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition


# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)


def listsandloops():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


# this is test driver or code that plays when executed directly, versus import which will not run these statements
def recursiveFactorialDriver():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
