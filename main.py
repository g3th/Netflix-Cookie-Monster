from options import browser_init
from gui import user_interface

if __name__ == "__main__":
    while True:
        interface = user_interface()
        if interface == "q":
            print("Quitting.")
            exit()
        else:
            options = browser_init()
            match interface:
                case "1":
                    filename = input("Enter file name (i.e. file.txt):")
                    options.launch()
                    options.option_one(filename, 0)
                case "2":
                    options.option_two()
                case "3":
                    options.option_three()
                case "4":
                    filename = input("Enter file name (i.e. file.json):")
                    options.option_four(filename)
                case _:
                    options.invalid()
