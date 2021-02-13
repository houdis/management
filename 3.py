from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.PhantomJS('/script/download/phantomjs')
browser.implicitly_wait(5)
browser.get('https://member.melon.com/muid/family/ticket/login/web/login_inform.htm')

username = browser.find_element_by_name('id') 
username.send_keys('houdis') 
 
password = browser.find_element_by_name('pwd') 
password.send_keys('rlagnswn1!')

browser.execute_script("document.getElementById('btnLogin').click()")

time.sleep(1)

browser.get('http://ticket.melon.com/performance/index.htm?prodId=200967')
browser.execute_script("seatReservation('200967','PT0001')")
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) 

browser.save_screenshot('screen2.png')