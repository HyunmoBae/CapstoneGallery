import pyautogui

#for w in pyautogui.getAllWindows():
#    print(w) #모든 윈도우를 가져오기

for w in pyautogui.getWindowsWithTitle("메모장"):
    print(w)

#    if w.isActive == False: #현재 활성화되지 않았다면
#       w.activate() #활성화 시키기

#    if w.isMaximized == False: #현재 최대크기가 아니라면
#        w.maximize() #최대크기로 변경

#    if w.isMinimized == False: #현재 최대크기가 아니라면
#        w.minimize() #최대크기로 변경

for w in pyautogui.getWindowsWithTitle("메모장"):
    w.activate()

    pyautogui.sleep(1)
    pyautogui.write("12345!")
    #pyautogui.write("Daegu Catholic University",interval=0.25)

    # pyautogui.write(["t","e","s","t","left","right","1","enter"],interval=0.25)

    # pyautogui.keyDown("shift") #누르고있기
    # pyautogui.press("4") 
    # pyautogui.keyUp("shift") #올리기

    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("a")
    # pyautogui.keyUp("a")
    # pyautogui.keyUp("ctrl")

    pyautogui.mouseInfo() #좌표값 찾기
    pyautogui.hotkey("ctrl","a")








