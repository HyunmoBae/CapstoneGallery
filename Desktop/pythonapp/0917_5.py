#주간 보고서 (1~50주차)
# 1주차 보고서
# 부서 :
# 이름 :
# 업무내용 :

for i in range(1,51):
    with open(str(i) + "주차 보고서.txt","w",encoding="utf8") as report_file:
        report_file.write(":::::::: {0} 주차 보고서 ::::::::".format(i))
        report_file.write("\n\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무내용 : ")
