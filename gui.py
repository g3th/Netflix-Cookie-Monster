def user_interface():
    print("\033[38;5;33m\n+-------------------------------------------------------------------+")
    print("|\33[38;5;11m   Cookies should be in Netscape Format, i.e:                      \033[38;5;33m|")
    print("|\33[38;5;11m   'netflix.com    Value   Path   Value   Epoch    etc..'          \033[38;5;33m|")
    print("+-------------------------------------------------------------------+")
    print("|\33[38;5;255m 1) Load Existing Cookie                                           \033[38;5;33m|")
    print("|\33[38;5;255m 2) Acquire Cookie from Session (needs login credentials)          \033[38;5;33m|")
    print("|\33[38;5;255m 3) Load Folder with Multiple Cookies                              \033[38;5;33m|")
    print("+-------------------------------------------------------------------+")
    choice = input("\n\33[38;5;255mChoose an Option, 'q' to quit: ")
    return choice
