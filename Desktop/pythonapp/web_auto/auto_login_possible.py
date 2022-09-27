from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pyautogui


browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get("https://naver.com")
browser.maximize_window()

login = browser.find_element(By.CSS_SELECTOR,"#account > a")
login.click()

time.sleep(2)
id = browser.find_element(By.ID,"id")
id.click()
pyperclip.copy("tsi0520") #복사
pyautogui.hotkey("ctrl","v") 
#id.send_keys("tsi0520")
#pyautogui.write("tsi0520",interval=0.25) #타이핑(네이버 안뚫림)

time.sleep(1)

pw = browser.find_element(By.ID,"pw")
pw.click()
#pw.send_keys("123")
pyperclip.copy("123")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()








