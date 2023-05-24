import requests, html5lib, bs4, time

from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://annarbor.craigslist.org/search/zip#search=1~gallery~0~0"
driver.get(URL)
time.sleep(5)

page = driver.page_source

soup = bs4.BeautifulSoup(page, 'html5lib')

print(soup.prettify())