from header import header
from parser import parse_file

def user_interface():
    header()
    print("\033[38;5;33m\n+-------------------------------------------------------------------+")
    print("|\33[38;5;11m   Cookies should be in Netscape Format, i.e:                      \033[38;5;33m|")
    print("|\33[38;5;11m   'netflix.com    Value   Path   Value   Epoch    etc..'          \033[38;5;33m|")
    print("+-------------------------------------------------------------------+")
    print("|\33[38;5;255m 1) Check Single Cookie                                            \033[38;5;33m|")
    print("|\33[38;5;255m 2) Check Multiple Cookies                                         \033[38;5;33m|")
    print("|\33[38;5;255m 3) Acquire Cookie from Session (needs login credentials)          \033[38;5;33m|")
    print("|\33[38;5;255m 4) Double Check Stored Cookie Validity                            \033[38;5;33m|")
    print("+-------------------------------------------------------------------+")
    choice = input("\n\33[38;5;255mChoose an Option, 'q' to quit: ")
    return choice


def sub_menu(current_filename, current_file_number, total_files):
    netID = ""
    parser = parse_file()
    file_lines = parser.extract_cookie_information(current_filename)
    for file in file_lines:
        if file.split("\t")[5] == "NetflixId":
            netID = file.split("ct%")[1][0:37]
    header()
    print(
        "\x1bc\033[38;5;33m\n+---------------------------------------------------------------------------------------+")
    print(
        "|\33[38;5;11m Cookie files should end in '.txt'                                                     \033[38;5;33m|")
    print("+---------------------------------------------------------------------------------------+")
    print(
        "|\33[38;5;11m Cookies should be placed in the 'cookies' folder                                      \033[38;5;33m|")
    print("+---------------------------------------------------------------------------------------+")
    print("| File {} out of {} - NetflixID Starts with - {}      |".format(str(current_file_number + 1), str(total_files), netID))
    print("+---------------------------------------------------------------------------------------+")