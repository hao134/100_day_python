from selenium import webdriver
from selenium.webdriver.common.by import  By

chrome_driver_path = "/Users/huangshihao/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#### python org
driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME,"q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME,"python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

##### amazon product price
# amazon_url = "https://www.amazon.com/-/zh_TW/LEVOIT-%E7%A9%BA%E6%B0%A3%E6%B8%85%E6%B7%A8%E6%A9%9F-%E9%81%A9%E7%94%A8%E6%96%BC%E5%AE%B6%E5%BA%AD-PM2-5-99-97/dp/B08R794ZMX/ref=sr_1_2?keywords=air%2Bpurifier&qid=1648624590&sprefix=%E7%A9%BA%E6%B0%A3%2Caps%2C351&sr=8-2&th=1"
# amazon_url2 = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
# driver.get(amazon_url)
#
#
# price=driver.find_element(By.CLASS_NAME, "a-offscreen")
# print("Check",price.tag_name)
# print(price.get_attribute("innerHTML"))
#
# #driver.close()
# driver.quit()




