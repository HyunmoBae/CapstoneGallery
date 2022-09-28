from unittest import result
import pyautogui

print("시작합니다.")
pyautogui.countdown(3)

pyautogui.alert("업무자동화 시작.")
#result = pyautogui.confirm("계속 진행하시겠습니까?")
result = pyautogui.prompt("프로젝트 이름을 입력하세요")
result = pyautogui.prompt("암호를 입력하세요")
