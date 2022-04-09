from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os


CHROME_DRIVER_PATH = "/Users/huangshihao/Development/chromedriver"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ["USER_NAME"]
PASSWORD = os.environ["PASS_WORD"]

class InstaFollower:

    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(2)
        later = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')
        later.click()
        # sleep(5)
        # later2 = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[2]')
        # later2.click()


    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        sleep(2)
        ck_followers = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        ck_followers.click()
        sleep(2)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/div[3]/button[1]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
