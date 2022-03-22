import fire
from getpass import getpass
import json
from urllib.request import urlopen
# from .classmodule import Auth
# from .funcmodule import login
class Auth(object):
    def login(self, username = None):
        if username == None:
            username = input("Username: ")
        if username == None:
            print("A username is required")
            return
        pw = getpass("Password: ")
        return username, pw
def login(username = None):
    if username == None:
        username = input("Username: ")
    if username == None:
        print("A username is required")
        return
    pw = getpass("Password: ")
    return "Login"

def scrape_tag(appid = "12afbc439752499a6067721f9f35a3c4"):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    city = input("Enter Your City : ")
    url = f"{base_url}?q={city}&appid={appid}"
    try : 
       response = urlopen(url)
       # storing the JSON response 
       # from url in data_json
       data_json = json.loads(response.read())
       return data_json
    except : 
        print("enter correct city name")
    
    

class Pipeline(object):
    def __init__(self):
        self.weather = scrape_tag
        self.auth = Auth()
        self.login = login

if __name__ == '__main__':
    fire.Fire(Pipeline)