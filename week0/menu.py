# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

import matrix
import tree
import swap
from pattern import ship2

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
import os

main_menu = [
    ["Swap", "swap.py"],
    ["Matrix", "matrix.py"],
    ["Tree", "tree.py"],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
ships_sub_menu = [
    ["Unoptimized ship", "pattern/ship1.py"],
    ["Optimized ship", ship2.ship]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def ships_submenu():
    title = "Ships Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # blank line before the menu
    print()

    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # blank line after the menu
    print()

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    input("press enter to clear")
    os.system('cls' if os.name == 'nt' else 'clear')

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()