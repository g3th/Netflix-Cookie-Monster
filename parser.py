import os
from cookie_builder import construct_cookie


class parse_file:

    def __init__(self):
        self.directory = "cookies/"
        self.files_list = os.listdir("cookies/")
        self.valid_cookies_list = []

    def get_text_files(self):
        for file in self.files_list:
            if file.endswith(".txt"):
                self.valid_cookies_list.append(file)
        return self.valid_cookies_list

    def extract_cookie_information(self, filename):
        file_lines = []
        with open(self.directory + str(filename), 'r') as cookie_file:
            for line in cookie_file.readlines():
                if " " in line:
                    file_lines.append(line.replace(" ", "\t"))
                else:
                    file_lines.append(line)
        cookie_file.close()
        return file_lines


