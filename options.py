import json
import time
import os

from gui import sub_menu
from gui import multi_cookie_checker_info
from cookie_builder import construct_cookie
from header import header
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from parser import parse_file


class browser_init:

    def __init__(self):
        time_now = str(datetime.now())
        posix_day = 86400
        self.parse_file = parse_file()
        self.valid_directory = "valid_cookies/"
        self.multi_checker_is_running = False
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

    def option_one(self, filename):
        file_lines = self.parse_file.extract_cookie_information(filename)
        cookie = construct_cookie()
        cookie.assign_values(file_lines)
        netflix_c = cookie.save_cookie(self.expiry)
        try:
            with open("cookies/netflix.json", 'r') as netflix_cookie:
                cookie = json.load(netflix_cookie)
                for obj in cookie:
                    self.browser.add_cookie(obj)
            netflix_cookie.close()
            time.sleep(1)
            self.browser.refresh()
            time.sleep(1)
            if not self.multi_checker_is_running:
                if (self.browser.find_elements(By.XPATH, '//div[@class="profiles-gate-container"]') or
                        self.browser.find_elements(By.XPATH,
                                                   "//div[@class='ptrack-container billboard-presentation-tracking']")):

                    print("Login was valid.")
                    input("Press Enter to return to Menu (i.e. after browsing, device registration etc..)")
                    with open("valid_cookies/" + str(filename.replace(".txt", ".json")), 'w') as write_cookie:
                        json.dump(netflix_c, write_cookie, indent=3)
                    write_cookie.close()
                else:
                    print("Login was invalid.")
                    input("Press Enter to return to Menu")
            elif self.multi_checker_is_running:
                if (self.browser.find_elements(By.XPATH, '//div[@class="profiles-gate-container"]') or
                        self.browser.find_elements(By.XPATH,
                                                   "//div[@class='ptrack-container billboard-presentation-tracking']")):
                    print("\033[38;5;10m    ✔ \033[38;5;33m|")
                else:
                    print("\033[38;5;9m    X \033[38;5;33m|")
                print("\033[38;5;33m+---------------------------------------------------------------------------------------+")
            self.browser.close()
        except FileNotFoundError:
            print("File Not Found. Double Check and try again.")
            input("Press Enter")
            print("\x1bc")

    def option_two(self):
        self.multi_checker_is_running = True
        cookie_filenames = self.parse_file.get_text_files()
        counter = 0
        print("\x1bc")
        header()
        multi_cookie_checker_info()
        while counter < len(cookie_filenames):
            sub_menu(cookie_filenames[counter], counter, len(cookie_filenames))
            browser_init.launch(self)
            browser_init.option_one(self, cookie_filenames[counter])
            counter += 1
        self.multi_checker_is_running = False
        input("\n\033[38;5;11mDone. Press Enter to return to Menu")

    def option_three(self):
        print("TODO")
        input("Press enter...")
        print("\x1bc")

    def option_four(self, filename):
        browser_init.launch(self)
        with open(self.valid_directory + str(filename), 'r') as read_cookie:
            cookie_jar = json.load(read_cookie)
            for cookie in cookie_jar:
                self.browser.add_cookie(cookie)
            time.sleep(0.7)
        read_cookie.close()
        self.browser.refresh()
        time.sleep(0.8)
        if (self.browser.find_elements(By.XPATH, '//div[@class="profiles-gate-container"]') or
                self.browser.find_elements(By.XPATH,
                                           "//div[@class='ptrack-container billboard-presentation-tracking']")):
            print("Login was valid.")
            input("Press Enter to return to Menu (i.e. after browsing, device registration etc..)")
        else:
            print("Login was invalid.")

    def help(self):
        print("Help")

    def invalid(self):
        print("Invalid Input.")
        input("Press enter...")
        print("\x1bc")
