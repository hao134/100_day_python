from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/huangshihao/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


### wekipedia part
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_numbers = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# # article_numbers.click()
#
# all_portals = driver.find_element(By.LINK_TEXT,"All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

### automatically write user information of a web
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME,"fName")
fname.send_keys("Shih Hao")
lname = driver.find_element(By.NAME,"lName")
lname.send_keys("Huang")
email = driver.find_element(By.NAME,"email")
email.send_keys("hsh319ab@gmail.com")
#sing_up_button = driver.find_element(By.XPATH,"/html/body/form/button")
# or
sing_up_button = driver.find_element(By.CSS_SELECTOR,"form button")
sing_up_button.click()

