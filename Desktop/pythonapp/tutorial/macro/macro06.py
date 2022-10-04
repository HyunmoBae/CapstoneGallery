from time import sleep
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get("https://naver.com")
browser.maximize_window()

#pyautogui.mouseInfo() #좌표값 찾기tsi0520
#stop

sleep(1)
pyautogui.click(1317,470)

sleep(1)
pyautogui.click(930,400)

sleep(1)
pyperclip.copy("tsi0520") #복사
pyautogui.hotkey("ctrl","v")

sleep(1)
pyautogui.click(960,450)

sleep(1)
pyperclip.copy("1234") #복사
pyautogui.hotkey("ctrl","v")

sleep(1)
pyautogui.click(950,560)

sleep(1)
browser.get("https://mail.naver.com")

sleep(1)
browser.find_element(By.CSS_SELECTOR,"#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault").click()

#받는사람
sleep(1)
pyautogui.write("tsi0520@naver.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
sleep(1)

pyperclip.copy("자동 메일 발송입니다.")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")
sleep(1)

pyperclip.copy("본문내용 입니다..")
pyautogui.hotkey("ctrl","v")
sleep(1)

browser.find_element(By.ID,"sendBtn").click()
sleep(2)
browser.quit()