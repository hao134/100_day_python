from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/huangshihao/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

count = 0
# grandma_value = driver.find_element(By.CSS_SELECTOR,"#buyGrandma b")
# print(grandma_value.text.split()[2])
timeout = time.time() + 60
nowtime = time.time() + 5
addfuncs = driver.find_element(By.ID,"store")
def add_funcs():
    addfuncs_list = [int(item.split()[-1].replace(',','')) for i, item in enumerate(addfuncs.text.split("\n")) if "-" in item]
    return addfuncs_list

def find_max(money, fun_list):
    for item in fun_list:
        if money < item:
            item_index = fun_list.index(item) - 1
            return fun_list[item_index], item_index
def find_id_name(id):
    if id == 0:
        return "buyCursor"
    elif id == 1:
        return "buyGrandma"
    elif id == 2:
        return "buyFactory"
    elif id == 3:
        return "buyMine"
    elif id == 4:
        return "buyShipment"
    elif id == 5:
        return "buyAlchemy lab"
    elif id == 6:
        return "buyPortal"
    elif id == 7:
        return "buyTime machine"
    else:
        return "buyElder Pledge"


while True:
    #time.sleep(0.1)
    cookie_click = driver.find_element(By.XPATH,'//*[@id="cookie"]')
    cookie_click.click()
    count += 1
    if time.time() > nowtime:
        test_list = add_funcs()
        print(test_list)
        cookies_num = driver.find_element(By.ID,"money")
        cookies_num = int(cookies_num.text.replace(',',''))
        cost, cost_index = find_max(money=cookies_num,fun_list=test_list)
        id_name = find_id_name(cost_index)
        print(cost_index)
        click = driver.find_element(By.ID, id_name)
        click.click()
        nowtime = time.time() + 5
    if time.time() > timeout:
        break


driver.quit()