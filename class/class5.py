from selenium import selenium
from selenium import wevdriver
from selenium.common.exeotion import NoSuchElementException
from selenium.wevdriver.common.Keys import Keys
import time
from bs4 import BeautifulSoup

browser = webdriver.GoogleChrome()
broswer.get('')
soup = BeautifulSoup(browser.page_source)
while len(soup.select('.pager-right'))>0
    for ele in soup.select('.hotel-info Header h3'):
        print ele.text 
    browser.find_element_by_linkxxxxxx
browser.close
#爬虫url:https://www.agoda.com/zh-cn/world.html?cid=-38