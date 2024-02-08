from options import browser_init
from header import header
from gui import user_interface

if __name__ == "__main__":
    header()
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
                    options.option_one(filename)
                case "2":
                    options.option_two()
                case _:
                    options.invalid()
