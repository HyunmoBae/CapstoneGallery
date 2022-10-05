from flask import Flask, render_template, request, redirect
import pymysql

#데이터베이스 연결
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="autoset",
                       database="dcu",
                       charset="UTF8"
                       )

cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/index.html")

#게시판 글 목록 
@app.route("/board/list")
def list():
    sql ="select * from board order by wdate desc"
    cur.execute(sql)

    rows = cur.fetchall()
    return render_template("/board/list.html",rows=rows)

#게시판 글 쓰기
@app.route("/board/write")
def write():
    return render_template("/board/write.html")    

#게시판 글 처리
@app.route("/board/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        name = request.form["name"]
        email = request.form["email"]
        memo = request.form["memo"]
        pw = request.form["pass"]

        sql = f"insert into board(title,name,email,memo,pw) values('{title}','{name}','{email}','{memo}','{pw}')"
        cur.execute(sql)
        conn.commit()
        return redirect('/board/list')

if __name__ == "__main__":
    # app.run(host="localhost",port="8200",debug=True)
    app.run()