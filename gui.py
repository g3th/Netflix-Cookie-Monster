from header import header


def user_interface():
    header()
    print("\033[38;5;33m\n+-------------------------------------------------------------------+")
    print("|\33[38;5;11m   Cookies should be in Netscape Format, i.e:                      \033[38;5;33m|")
    print("|\33[38;5;11m   'netflix.com    Value   Path   Value   Epoch    etc..'          \033[38;5;33m|")
    print("+-------------------------------------------------------------------+")
    print("|\33[38;5;255m 1) Load Existing Cookie                                           \033[38;5;33m|")
    print("|\33[38;5;255m 2) Acquire Cookie from Session (needs login credentials)          \033[38;5;33m|")
    print("|\33[38;5;255m 3) Check Multiple Cookies                                         \033[38;5;33m|")
    print("+-------------------------------------------------------------------+")
    choice = input("\n\33[38;5;255mChoose an Option, 'q' to quit: ")
    return choice


def sub_menu(current_file, total_files, filename):
    with open("cookies/" + str(filename), 'r') as cookie_lines:
        for line in cookie_lines.readlines():
            if line.split("\t")[5] == "NetflixId":
                netID = line.split("ct%")[1][0:37]
    cookie_lines.close()
    header()
    print(
        "\x1bc\033[38;5;33m\n+---------------------------------------------------------------------------------------+")
    print(
        "|\33[38;5;11m Cookie files should end in '.txt'                                                     \033[38;5;33m|")
    print("+---------------------------------------------------------------------------------------+")
    print(
        "|\33[38;5;11m Cookies should be placed in the 'cookies' folder                                      \033[38;5;33m|")
    print("+---------------------------------------------------------------------------------------+")
    print("| File {} out of {} - NetflixID Starts with - {}     |".format(str(current_file + 1), str(total_files), netID))
    print("+---------------------------------------------------------------------------------------+")
