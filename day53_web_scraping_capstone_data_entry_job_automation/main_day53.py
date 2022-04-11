import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

headders = {
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.50498919634178%2C%22east%22%3A-122.38293795732811%2C%22south%22%3A37.704180842811965%2C%22north%22%3A37.813973601334574%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A474579%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"
zillow_url2 = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
response = requests.get(zillow_url2, headers = headders)
zillow_page = response.text
soup = BeautifulSoup(zillow_page,"lxml")
print(soup.title)


house_prices_list = []
house_address_list = []
house_link_list = []
house_data = []
house_prices = soup.select(selector = "div.list-card-info div.list-card-price")
house_addrs = soup.select(selector = "div.list-card-info address.list-card-addr")
house_links = soup.select(selector = "div.list-card-info a.list-card-link")
for price in house_prices:
    house_prices_list.append(price.text)

for addr in house_addrs:
    house_address_list.append(addr.text)

for link in house_links:
    house_link_list.append(link.get("href"))

# print(house_prices_list)
# print(house_address_list)
# print(house_link_list)

for num in range(len(house_prices_list)):
    element = {}
    element['price'] = house_prices_list[num]
    element['address'] = house_address_list[num]
    element['link'] = house_link_list[num]
    house_data.append(element)


############## selenium part
google_sheet_url = "https://docs.google.com/forms/d/e/1FAIpQLSetSqhTrXklZIhbrpqicihGZq97NkJ-bj6KkR0pFcpcW_OV_A/viewform"
CHROME_DRIVER_PATH = "/Users/huangshihao/Development/chromedriver"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(google_sheet_url)

for num in range(len(house_data)):
    sleep(2)
    address_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(house_data[num]['address'])
    price_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(house_data[num]['price'])
    link_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_text = house_data[num]['link']
    if "https" not in link_text:
        link_text = "https://www.zillow.com" + link_text
    link_field.send_keys(link_text)
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
    sleep(2)
    another_response = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()





sleep(2)
driver.quit()


