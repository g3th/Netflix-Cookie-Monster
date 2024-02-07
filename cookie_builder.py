import json


# Selenium will fail to read specific keys, unless they are exactly as specified in 'webdriver.py' test conditions (
# line 631). If these keys are slightly different, it will either throw "AssertionError" or "unable to set cookie."
# These dict keys are:
#
# "sameSite": - one of "None", "Strict" or "Lax" - first letter capitalized and quotes included in the file
# "httpOnly" and "hostOnly" - both should have first letter capitalized
# "secure" is capitalized

def cookie_objects(expiration, secure_netflix_id, netflix_id, pas, opt_anon, flwssn, nfvdid, onetrust):
    cookie_data = {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "netflix-sans-normal-3-loaded",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "true"
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'true',
        "name": 'SecureNetflixId',
        "path": "/",
        "sameSite": 'Strict',
        "Secure": 'true',
        "session": 'false',
        "storeId": 'null',
        "value": secure_netflix_id
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "hasSeenCookieDisclosure",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "true"
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "profilesNewSession",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "0"
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'true',
        "name": "NetflixId",
        "path": "/",
        "sameSite": "Lax",
        "Secure": 'true',
        "session": 'false',
        "storeId": 'null',
        "value": netflix_id
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false,',
        "name": "pas",
        "path": "/",
        "sameSite": "None",
        "Secure": 'false,',
        "session": 'false',
        "storeId": 'null',
        "value": pas
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "OptanonConsent",
        "path": "/",
        "sameSite": "Lax",
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": opt_anon
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "HostOnly": 'false',
        "HttpOnly": 'false',
        "name": "dsca",
        "path": "/",
        "sameSite": "None",
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "customer"
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "dsca",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "customer"
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "flwssn",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": flwssn
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "netflix-sans-bold-3-loaded",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "true"
    }, {
        "domain": ".netflix.com",
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "nfvdid",
        "path": "/",
        "sameSite": 'None',
        "Secure": 'false',
        "session": 'true',
        "storeId": 'null',
        "value": nfvdid
    }, {
        "domain": ".netflix.com",
        "expirationDate": expiration,
        "hostOnly": 'false',
        "HttpOnly": 'false',
        "name": "OptanonAlertBoxClosed",
        "path": "/",
        "sameSite": "Lax",
        "Secure": 'false',
        "session": 'false',
        "storeId": 'null',
        "value": "2024-02-03T01:05:45.269Z"
    }
    return cookie_data


class construct_cookie:

    def __init__(self, file):
        self.filename = file
        self.netID = ""
        self.secure = ""
        self.opt = ""
        self.nfvdid = ""
        self.flwssn = ""
        self.pas = ""

    def assign_values(self):
        with open(self.filename, 'r') as cookie_file:
            for line in cookie_file.readlines():
                if line.split("\t")[5] == "NetflixId":
                    self.netID = line.split("\t")[6].strip()
                if "OptanonConsent" in line:
                    self.opt = line.split("\t")[6].strip()
                if "SecureNetflixId" in line:
                    self.secure = line.split("\t")[6].strip()
                if "nfvdid" in line:
                    self.nfvdid = line.split("\t")[6].strip()
                if "flwssn" in line:
                    self.flwssn = line.split("\t")[6].strip()
                if "pas" in line:
                    self.pas = line.split("\t")[6].strip()

    def acquire_cookie(self, browser):
        with open(self.filename, 'w') as cookie:
            json.dump(browser.get_cookies(), cookie, indent=3)
        cookie.close()

    # expiration, Secure_netflix_id, netflix_id, pas, opt_anon, flwssn, nfvdid, onetrust
    def save_cookie(self, expiration, onetrust):
        netflix_cookie = cookie_objects(expiration, self.secure, self.netID, self.pas, self.opt, self.flwssn,
                                        self.nfvdid, onetrust)
        with open("netflix.json", 'w') as write_cookie:
            json.dump(netflix_cookie, write_cookie, indent=3)
        write_cookie.close()
