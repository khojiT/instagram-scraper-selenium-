from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

import os
import wget

USER = input('USER')
PASS = input('PASS')
search = input('what is your search?')
x = int(input('How many posts want to check?'))

driver = webdriver.Chrome(executable_path='C:\\Users\\persian\\Desktop\\chromedriver.exe')
driver.maximize_window()
url = 'https://www.instagram.com/'
driver.get(url)
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'password']")))
username.clear()
password.clear()
username.send_keys(USER)
password.send_keys(PASS)
login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
search_box = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder = 'Search']")))
search_box.clear()
keyword = 'search'
search_box.send_keys(keyword)
time.sleep(10)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class = '_9AhH0']"))).click()
time.sleep(5)

l_caption = []
c = 0
i =0
while c < x:
    time.sleep(2)
    image = driver.find_elements_by_class_name('FFVAD')[c]
    src = image.get_attribute('src')
    save = os.path.join('E:\\web', keyword + str(c) + '.jpg')
    wget.download(src, save)
    caption =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span")))
    l_caption = l_caption + [caption.text]
    c += 1
    time.sleep(5)
    next = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Next')]"))).click()
for item in l_caption:
    print(item)
    print('\n\n\n\n')
driver.quit()
