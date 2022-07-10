#   Required Framework
# pip install selenium
# pip install webdriver-manager

KEYWORD = 'bbq grill'


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
import os
import random
import csv

def get_and_wait_element(browser, xpath, sec_wait=10):
    WebDriverWait(browser, sec_wait).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )

    return browser.find_element(By.XPATH, xpath)

def get_and_wait_elements(browser, xpath, sec_wait=10):
    WebDriverWait(browser, sec_wait).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )

    return browser.find_elements(By.XPATH, xpath)

def ini_browser():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    opts = Options()
    opts.add_argument("user-agent=" + USER_AGENT)
    s=Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=opts)
    return browser

browser = ini_browser()

url = "https://www.amazon.com/s?k=" + KEYWORD

# open the browser
browser.get(url)
browser.maximize_window()

global links

global splited_brand

links = []

global next_page

#close_address = get_and_wait_element(browser, '/html/body/div[1]/header/div/div[4]/div[1]/div/div/div[3]/span[1]/span/input')
#close_address.click()

time.sleep(5)

while True:
	list_results = browser.find_elements(by=By.CLASS_NAME, value="a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
	for link in list_results:
		if link in links:
			pass
		else:
			links.append(link.get_attribute("href"))
	
#	browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#	time.sleep(5)
#	browser.execute_script("window.scrollTo(0, 6500)")
	
	time.sleep(5)
	
	#browser.execute_script("arguments[0].scrollIntoView();", next_page)
	
	try:
		next_page = browser.find_element(by=By.CLASS_NAME, value="company__link")
		browser.execute_script("arguments[0].scrollIntoView();",next_page)
		time.sleep(10)
		next_page.click()
	except:
		break	

print(len(links))

no_repeats = list(set(links)) 

randlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(len(no_repeats))

for newlink in no_repeats:
	time.sleep(random.choice(randlist))
	print(newlink)
	try:
		browser.get(str(newlink))
		time.sleep(5)
		#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
		brand = browser.find_element(By.ID, "bylineInfo").text
		brandone = str(brand)
		print(brand)
		print(brandone)
		splited_brand = brandone.split(" ")
		print(splited_brand)
		words = ["Visit", "the", "Store", "Brand:"]
		for word in words:
			if word in splited_brand:
				splited_brand.remove(word)
		print(' '.join(splited_brand))
		with open('brands.csv', 'a') as csvfile: 
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow([' '.join(splited_brand)])
			
	except:
		pass





