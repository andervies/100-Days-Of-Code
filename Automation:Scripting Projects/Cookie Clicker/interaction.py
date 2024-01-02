from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def buy_item():
    affordable_upgrades = {}
    for price, item_id in ids_and_prices.items():
        if money > price:
            affordable_upgrades[price] = item_id
    highest_price = max(affordable_upgrades)
    highest_id = affordable_upgrades[highest_price]
    driver.find_element(By.ID, highest_id).click()




# driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# print(driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a").text)

# driver.get("https://secure-retreat-92358.herokuapp.com/")
# f_name = driver.find_element(By.NAME, "fName")
# f_name.send_keys("Ander")
# l_name = driver.find_element(By.NAME, "lName")
# l_name.send_keys("Nojan")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("anderclace@gmail.com")
# # email.send_keys(Keys.ENTER)

# driver.implicitly_wait(50)

# big_cookie = driver.find_element(By.ID, "bigCookie")

# WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div style display block")))


driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")
element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'cookie')))
timeout = time.time() + 30
sleep = time.time() + 5
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in store_items]
item_prices = [driver.find_elements(By.CSS_SELECTOR, "#store b")]

prices = [int(price.text.strip().split("-")[1].replace(",", "")) for price in item_prices[0] if price.text != ""]

ids_and_prices = {}
for n in range(len(prices)):
    ids_and_prices[prices[n]] = item_ids[n]


is_game_on = True


while is_game_on:
    element.click()
    if time.time() > sleep:
        sleep = time.time() + 5
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        buy_item()
    if time.time() > timeout:
        is_game_on = False

driver.quit()

