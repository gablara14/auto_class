import webbrowser
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from classes import getClassURL 
from keys import keys
import time


login_url = 'https://graduacao.mackenzie.br/login/index.php'


class MackBot:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.current_class = getClassURL()
        self.current_elo = getClassURL("elo")


    def login(self):
        bot = self.bot
        bot.get(login_url)
        time.sleep(3)

        username = bot.find_element_by_id('username')
        password = bot.find_element_by_id("password")
        username.clear()
        password.clear()

        username.send_keys(self.username)
        password.send_keys(self.password)
        password.submit()
        time.sleep(3)
    
    def openClass(self):
        bot = self.bot
        current = self.current_class
        bot.get(current)
    
    def openElo(self):
        bot = self.bot
        current_elo = self.current_elo
        time.sleep(2)
        script_ = '''window.open("{}","_blank");'''.format(current_elo)
        bot.execute_script(script_)

    def openEloClass(self):
        bot = self.bot
        time.sleep(3)
        test = bot.find_elements_by_xpath("//*[contains(text(), '09:00')]")
        print(test)
        
        


user = MackBot(keys["username"], keys["password"])
user.login()
user.openClass()
user.openElo()
#user.openEloClass()
#user.like_tweet('artigo')