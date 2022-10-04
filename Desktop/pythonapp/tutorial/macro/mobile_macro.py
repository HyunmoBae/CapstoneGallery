import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

url = "https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/"

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get(url)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized') 
# --window-size=x,y / --start-maximized / --mute-audio(음소거)

time.sleep(2)
id = browser.find_element(By.ID,"id")
id.click()
pyperclip.copy("tsi0520") #복사
pyautogui.hotkey("ctrl","v")

time.sleep(2)
pw = browser.find_element(By.ID,"pw")
pw.click()
pyperclip.copy("qo1692313!")
pyautogui.hotkey("ctrl","v")

time.sleep(1)
login = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login.click()

time.sleep(1)
browser.get("https://m.blog.naver.com/FeedList.naver")
time.sleep(1)
browser.get("https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FFeedList.naver")

time.sleep(1)
title = browser.find_element(By.CSS_SELECTOR,"#se_component_wrapper > div:nth-child(1) > div > div.se_sectionArea.se_align-left > div > div > div > div > textarea")
title.click()
title.send_keys("제목")

time.sleep(1)
memo = browser.find_element(By.CSS_SELECTOR,"#se_component_wrapper > div:nth-child(2) > div > div > div > div.se_viewArea.se_ff_nanumgothic.se_align-left.se_fs_T3 > div > div > div > div")
memo.click()
memo.send_keys("내용임")
time.sleep(1)
memo.send_keys(Keys.ENTER)
memo.send_keys("두번째내용임")

time.sleep(1)
write = browser.find_element(By.CSS_SELECTOR,"#editor_frame > div > div.editor-container > div.header-container > div.editor-header > button.btn_applyPost")
write.click()
