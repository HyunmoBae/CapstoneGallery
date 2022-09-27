import csv

f = open('file.csv','w',encoding='utf-8-sig',newline='') #newline 안하면 두줄띄움
wr = csv.writer(f)
wr.writerow([1,"삼성전자"])
wr.writerow([2,"LG화학"])

f.close()







