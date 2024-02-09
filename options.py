import json
import time
import os

import gui
from gui import sub_menu
from cookie_builder import construct_cookie
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from parser import parse_file


class browser_init:

    def __init__(self):
        time_now = str(datetime.now())
        posix_day = 86400
        self.cookie_directory_files = os.listdir("cookies/")
        self.expiry = time.time() + posix_day * 365
        self.time_parsed_onetrust = time_now.split(" ")[0] + "T" + time_now.split(" ")[1][0:-3] + "Z"
        self.cookie_assign_value = ""
        self.page = "https://www.netflix.com/browse"
        self.browser_options = Options()
        self.browser_options.add_argument("--headless=new")
        self.browser = webdriver.Chrome(options=self.browser_options)
        self.browser.close()

    def launch(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.page)
        self.browser.set_window_size(300, 600)
        time.sleep(0.7)

    def option_one(self, filename, counter):
        cookie = construct_cookie(filename)
        cookie.assign_values(counter)
        netflix_cookie = cookie.save_cookie(self.expiry)
        try:
            with open("cookies/netflix.json", 'r') as netflix_cookie:
                cookie = json.load(netflix_cookie)
                for obj in cookie:
                    self.browser.add_cookie(obj)
            netflix_cookie.close()
            time.sleep(1)
            self.browser.refresh()
            time.sleep(1)
            if (self.browser.find_elements(By.XPATH, '//div[@class="profiles-gate-container"]') or
                    self.browser.find_elements(By.XPATH,
                                               "//div[@class='ptrack-container billboard-presentation-tracking']")):
                with open("valid_cookies/" + str(filename), 'w') as write_cookie:
                    json.dump(netflix_cookie, write_cookie, indent=3)
                write_cookie.close()
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
        print("TODO")
        input("Press enter...")
        print("\x1bc")

    def option_three(self):
        parser = parse_file()
        cookie_filenames = parser.get_text_files()
        counter = 0
        while counter < len(cookie_filenames):
            sub_menu(counter, len(cookie_filenames), cookie_filenames[counter])
            browser_init.launch(self)
            browser_init.option_one(self, cookie_filenames[counter], counter)
            counter += 1


    def invalid(self):
        print("Invalid Input.")
        input("Press enter...")
        print("\x1bc")
