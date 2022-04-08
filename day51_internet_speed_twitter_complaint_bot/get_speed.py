from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

chrome_driver_path = "/Users/huangshihao/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://speed5.ntu.edu.tw/speed5/")
sleep(3)
start_button = driver.find_element(By.ID,"btn")
start_button.click()

sleep(20)
download_speed = driver.find_element(By.ID, "download_text")
print(download_speed.text)
sleep(8)
upload_speed = driver.find_element(By.ID, "upload_text")
print(upload_speed.text)
