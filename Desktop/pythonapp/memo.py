from tkinter import *

window = Tk()
window.title("*제목없음*")
window.geometry("640x480")

def new_file():
    print("새 파일을 생성합니다.")

menu = Menu(window)

#파일
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="새 항목(N)",command=new_file())
menu_file.add_command(label="새 창(shift+N)")
menu_file.add_command(label="열기(O)")
menu_file.add_command(label="저장(S)")
menu_file.add_command(label="다른이름으로 저장(shift+S)")
menu_file.add_separator()
menu_file.add_command(label="페이지 설정")
menu_file.add_command(label="인쇄")
menu_file.add_separator()
menu_file.add_command(label="종료",command=quit)

#편집
menu_edit = Menu(menu,tearoff=0)
menu_edit.add_command(label="실행취소(U)",state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="잘라내기(X)",state="disable")
menu_edit.add_command(label="복사(C)",state="disable")
menu_edit.add_command(label="붙여넣기(P)")
menu_edit.add_command(label="삭제(D)",state="disable")

#서식
menu_doc = Menu(menu,tearoff=0)
menu_doc.add_checkbutton(label="자동 행 바꿈")
menu_doc.add_command(label="글꼴")

#보기
menu_view = Menu(menu,tearoff=0)
menu_view.add_radiobutton(label="확대(I)")
menu_view.add_radiobutton(label="축소(O)")

menu.add_cascade(label="파일(F)",menu=menu_file)
menu.add_cascade(label="편집(E)",menu=menu_edit)
menu.add_cascade(label="서식(O)",menu=menu_doc)
menu.add_cascade(label="보기(V)",menu=menu_view)
menu.add_cascade(label="도움말(H)")

window.config(menu=menu)

window.mainloop()