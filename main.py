class Menu:
    def __init__(self):
        border = "=" * 25
        self.banner = f"\n{border}\nPlease Select An Option\n{border}"

        self.main_menu = [
            ["Week 0", "self.buildMenu('Week 0 ' + self.banner, self.week0)"],
            ["Week 1", "self.buildMenu('Week 1 ' + self.banner, self.week1)"],
            ["Week 2", "self.buildMenu('Week 2 ' + self.banner, self.week2)"],
        ]
        self.week0 = [
            ["Swap", "swap.py"],
            ["Matrix", "matrix.py"],
            ["Tree", "tree.py"],
            ["Ships Sub-Menu", "self.buildMenu('Ships Sub-Menu ' + self.banner, self.ship_submenu)"]
        ]
        self.ship_submenu = [
            ["Unoptimized ship", "pattern/ship1.py"],
            ["Optimized ship", "pattern/ship2.py"]
        ]
        self.week1 = [
            ["Loops Tester", ""]
        ]
        self.week2 = [
            []
        ]

    def __call__(self):
        self.buildMenu("Main Menu " + self.banner, self.main_menu)

    def buildMenu(self, banner, options):
        print()
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
        choice = input("Type your choice: ")
        print()

        try:
            choice = int(choice)
            if choice == 0:
                # stop
                return
            try:
                eval(prompts.get(choice)[1])
            except:
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
                input("Press Enter to Clear")
        except ValueError:
            # not a number error
            print(f"Not a number: {choice}")
            input("Press Enter to Clear")
        except UnboundLocalError:
            # traps all other errors
            print(f"Invalid choice: {choice}")
            input("Press Enter to Clear")
        # end validation try

        self.buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu = Menu()
    menu()