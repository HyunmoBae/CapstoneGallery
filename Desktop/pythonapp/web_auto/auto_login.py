from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
time.sleep(2)

# browser.implicitly_wait(10) #로딩 후 10초 대기
browser.maximize_window() #화면 최대화
id = browser.find_element(By.CSS_SELECTOR, "#id")
id.click()
id.send_keys("tsi0520")

time.sleep(2)

pw = browser.find_element(By.CSS_SELECTOR,'#pw')
pw.click()
pw.send_keys("1234!")

login = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login.click()