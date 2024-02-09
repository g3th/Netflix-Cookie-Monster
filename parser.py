import os
from cookie_builder import construct_cookie


class parse_file:

    def __init__(self):
        self.files_list = os.listdir("cookies/")
        self.valid_cookies_list = []

    def get_text_files(self):
        for file in self.files_list:
            if file.endswith(".txt"):
                self.valid_cookies_list.append(file)
        return self.valid_cookies_list
