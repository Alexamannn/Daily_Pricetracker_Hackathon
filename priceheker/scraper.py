import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pandas.io.html import read_html
from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions, Chrome
from selenium import webdriver
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def xx(url):
 chrome_options = webdriver.ChromeOptions()
 chrome_options.add_experimental_option("detach", True)
 driver = webdriver.Chrome('C:/Users/39338/Downloads/chromedriver', chrome_options=chrome_options)
 driver.get(url)
 c=driver.find_element_by_xpath('//*[@id="a-autoid-0"]/span')
 c.click()
 zz = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[6]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span[1]')
 for i in zz:
  kk=[i.text]
  return kk
