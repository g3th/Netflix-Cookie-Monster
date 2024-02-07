import json
import time
from header import header
from datetime import datetime
from cookie_builder import construct_cookie
from selenium import webdriver
from selenium.webdriver.common.by import By

posix_day = 86400
expiry = time.time() + posix_day * 365
time_now = str(datetime.now())
time_parsed_onetrust = time_now.split(" ")[0] + "T" + time_now.split(" ")[1][0:-3] + "Z"
header()
print("\n\33[38;5;255mCookies should be in Netscape Format (or 'cookiejar')"
      "i.e:\n'netflix.com    Value   Path   Value   Epoch    etc..'\n")
print("1) Load Existing Cookie")
print("2) Acquire Cookie from Session (needs login credentials)\n")
while True:
    choice = input("Choose an Option, 'q' to quit: ")
    match choice:
        case "1":
            try:
                filename = str(input("Enter file name (i.e. file.txt):"))
                cookie = construct_cookie(filename)
                cookie.assign_values()
                # expiration, secure_netflix_id, netflix_id, pas, opt_anon, flwssn, nfvdid, onetrust
                cookie.save_cookie(expiry, time_parsed_onetrust)
                browser = webdriver.Chrome()
                page = "https://www.netflix.com/browse"
                browser.get(page)
                with open("netflix.json", 'r') as netflix_cookie:
                    cookie = json.load(netflix_cookie)
                    for obj in cookie:
                        browser.add_cookie(obj)
                netflix_cookie.close()
                time.sleep(0.7)
                browser.refresh()
                time.sleep(1)
                if (browser.find_elements(By.XPATH, '//div[@class="profiles-gate-container"]') or
                        browser.find_elements(By.XPATH, "//div[@class='ptrack-container billboard-presentation-tracking']")):
                    print("Login was valid.")
                    input("Press Enter to Terminate session (i.e. after browsing, device registration etc..)")
                else:
                    print("Login was invalid.")
                print("Done.")
                browser.close()
                exit()
            except FileNotFoundError as f:
                print(f)
                print("File Not Found. Double Check and try again.")
                input("Press Enter")
                print("\x1bc")
        case "2":
            print("TODO: This one")
            exit()
        case "q":
            print("Quitting.")
            exit()
        case _:
            print("Invalid Input")
            input("Press enter")
            print("\x1bc")
