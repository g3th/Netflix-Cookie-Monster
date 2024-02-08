import json
import time
from cookie_builder import construct_cookie
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class browser_init:

    def __init__(self):
        time_now = str(datetime.now())
        posix_day = 86400
        self.expiry = time.time() + posix_day * 365
        self.time_parsed_onetrust = time_now.split(" ")[0] + "T" + time_now.split(" ")[1][0:-3] + "Z"
        self.page = "https://www.netflix.com/browse"
        self.browser = webdriver.Chrome()
        self.browser.close()

    def launch(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.page)
        self.browser.set_window_size(300, 600)
        time.sleep(0.7)

    def option_one(self, filename):
        cookie = construct_cookie(filename)
        cookie.assign_values()
        cookie.save_cookie(self.expiry, self.time_parsed_onetrust)
        try:
            with open("cookies/netflix.json", 'r') as netflix_cookie:
                cookie = json.load(netflix_cookie)
                for obj in cookie:
                    self.browser.add_cookie(obj)
                # expiration, secure_netflix_id, netflix_id, pas, opt_anon, flwssn, nfvdid, onetrust
            netflix_cookie.close()
            time.sleep(1)
            self.browser.refresh()
            time.sleep(1)
            if (self.browser.find_elements(By.XPATH, '//div[@class="profiles-gate-container"]') or
                    self.browser.find_elements(By.XPATH, "//div[@class='ptrack-container billboard-presentation-tracking']")):
                print("Login was valid.")
                input("Press Enter to return to Menu (i.e. after browsing, device registration etc..)")
            else:
                print("Login was invalid.")
            print("Done.")
            self.browser.close()
        except FileNotFoundError:
            print("File Not Found. Double Check and try again.")
            input("Press Enter")
            print("\x1bc")

    def option_two(self):
        print("TODO: This one")
        input("Press enter...")
        print("\x1bc")

    def invalid(self):
        print("Invalid Input.")
        input("Press enter...")
        print("\x1bc")



