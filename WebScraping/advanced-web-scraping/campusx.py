# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("/home/soumya/Desktop/Tech/Python_Programming/PythonTutorials/WebScraping/advanced-web-scraping/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service = s)

driver.get('http://google.com')
time.sleep(1)

# fetch the search input box using xpath.
# xpath: path of the item in the webpage.
# xpath is a language to navigate through the html elements.
user_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
user_input.send_keys("Campusx")
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
link.click()
time.sleep(1)

link2 = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]")
link2.click()
time.sleep(1)