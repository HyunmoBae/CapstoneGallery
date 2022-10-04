import pyautogui

pyautogui.PAUSE=1 #모든 동작이 1초씩 대기

#for i in range(5):
    #pyautogui.move(100,100)

f= pyautogui.getActiveWindow() #현재 활성화된 창
print(f.title) #창의 제목
print(f.size)
print(f.left,f.top,f.right,f.bottom) #창의 좌표

pyautogui.click(f.left+200,f.top+20)



