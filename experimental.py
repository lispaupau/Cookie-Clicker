from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(10)

select_language = driver.find_element(By.XPATH, value='//*[@id="langSelect-RU"]')
select_language.click()

driver.implicitly_wait(20)

click_on_cookie = driver.find_element(By.ID, value='bigCookie')
cookies = driver.find_element(By.ID, value='cookies')


def check_condition():
    while True:
        time.sleep(5)
        cookies_count = float(cookies.text.split()[1].replace(',', ''))
        price_list = []
        for i in range(0, 19):
            product_price = driver.find_element(By.ID, value=f'productPrice{i}')
            if product_price.text == '':
                continue
            else:
                price_list.append(float(product_price.text.replace(',', '')))

        upgrade = driver.find_element(By.ID, value='upgrade0')
        upgrade.click()

        for price in range(len(price_list) - 1):
            if cookies_count >= price_list[price + 1]:
                buy_product = driver.find_element(By.ID, value=f'product{price_list.index(price_list[price + 1])}')
                buy_product.click()
            else:
                buy_product = driver.find_element(By.ID, value=f'product{price_list.index(price_list[price])}')
                buy_product.click()


condition_thread = threading.Thread(target=check_condition)
condition_thread.start()

while True:
    click_on_cookie.click()
