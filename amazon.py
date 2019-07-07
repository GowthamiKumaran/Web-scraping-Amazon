'''Web Scraping'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
BROWSER = webdriver.Chrome()
BASE_URL = "https://www.amazon.in/"
BROWSER.get(BASE_URL)
assert("Amazon.in" in BROWSER.title)
SEARCH_FIELD = BROWSER.find_element_by_name("field-keywords")
SEARCH_FIELD.clear()
SEARCH_FIELD.send_keys("umbrella")
SEARCH_FIELD.send_keys(Keys.RETURN)
SOURCE = BROWSER.page_source
SOUPOBJ = bs(SOURCE, 'lxml')
EXT1 = SOUPOBJ.find('a', {'title':'Red'})
URL = BASE_URL + EXT1['href'] 
BROWSER.get(URL)


