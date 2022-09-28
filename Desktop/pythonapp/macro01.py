from shutil import move
import pyautogui

#size = pyautogui.size() #현재 화면의 스크린 사이즈
#print(size)

#pyautogui.moveTo(200,100) #마우스 절대좌표 이동 (가로,세로,해당초)
#pyautogui.moveTo(100,200,duration=10) #5초동안 마우스 절대좌표 이동

pyautogui.moveTo(100,100, duration=0.25)
p = pyautogui.position()
print(p[0],p[1])
print(p.x,p.y)
pyautogui.moveTo(200,200, duration=0.25)
pyautogui.moveTo(300,300, duration=0.25)

pyautogui.move(100,100, duration=0.25)

print(pyautogui.position)
pyautogui.move(100,100,duration=0.25)
print(pyautogui.position)