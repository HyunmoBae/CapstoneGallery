import pyautogui

pyautogui.sleep(2) #2초대기
#print(pyautogui.position())
#pyautogui.click(94,22,duration=3) #마우스 해당 좌표로 이동 후 클릭
#pyautogui.mouseDown() #click
#pyautogui.mouseUp()


#pyautogui.doubleClick(208,448, duration=3)
#pyautogui.click(94,22,clicks=500,interval=1) #1초마다 클릭하라는 뜻
#pyautogui.rightClick(94,22,duration=2)
#pyautogui.middleClick(843,22,duration=2)

#pyautogui.moveTo(1200,307)
#pyautogui.drag(300,0,duration=0.25)#상대좌표 드래그
#pyautogui.dragTo(1500,607,duration=0.25)
#pyautogui.drag(300,0,duration=0.25)
#pyautogui.sleep(1)
#pyautogui.drag(0,300,duration=0.25)
#pyautogui.sleep(1)
#pyautogui.drag(-300,0,duration=0.25)
#pyautogui.sleep(1)
#pyautogui.drag(0,-300,duration=0.25)
pyautogui.scroll(-300) #음수 = 아래로 스크롤

