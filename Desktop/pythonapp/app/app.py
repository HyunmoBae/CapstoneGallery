from flask import Flask, render_template, request, redirect
import pymysql
import datetime as dt

#데이터베이스 연결
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="autoset",
                       database="dcu",
                       charset="UTF8"
                       )

cur = conn.cursor()

app = Flask(__name__)

####### 검색어 처리 ######### 
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == "POST":
        search = request.form['searchstring']
        sql = f"select * from board where title like '%{search}%' or name like '%{search}%' or memo like '%{search}%' order by wdate desc"
        cur.execute(sql)

        rows= cur.fetchall()
        print(rows)

        rows1 = []
        for i in rows:
            rows_dic = {
                'id' : i[0],
                'title' : i[1],
                'name' : i[2],
                'email' : i[3],
                'memo' : i[4],
                'wdate' : i[5],
                'hit' : i[6]
            }
            print(rows_dic)
            rows1.append(rows_dic)
            print(rows1)
        return render_template('board/search.html', rows=rows1)

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
        hit = 0
        wdate = dt.datetime.now()
        n_wdate = wdate.replace(microsecond=0)

        sql = f"insert into board(title,name,email,memo,pw,hit,wdate) values('{title}','{name}','{email}','{memo}','{pw}',{hit},'{n_wdate}')"
        cur.execute(sql)
        conn.commit()
        return redirect('/board/list')

#게시글 보기
@app.route('/board/contents/<int:id>')
def contents(id):
    sql1 = f"update board set hit = hit + 1 where id={id}"
    cur.execute(sql1)

    sql = f"select * from board where id={id}"
    cur.execute(sql)
    rows = cur.fetchall()
    return render_template("/board/contents.html",rows=rows[0])

####### 글 수정폼 #########
@app.route('/board/edit/<int:id>')
def edit(id):
    sql = f"select * from board where id={id}"
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    return render_template('board/edit.html', rows=rows[0])

####### 글 수정 처리 #########
@app.route('/board/editok',methods=["GET","POST"])
def editok():
    if request.method == "POST":
        id = request.form['id']
        title = request.form['title']
        name = request.form['name']
        email = request.form['email']
        memo = request.form['memo']
        pw = request.form['pass']

        sql1 = f"select * from board where id={id}"
        cur.execute(sql1)
        rows = cur.fetchall()

        print(rows[0][7])
        if pw ==rows[0][7]:

            sql = f"update board set title='{title}',name = '{name}',email = '{email}', memo = '{memo}' where id={id}"
            cur.execute(sql)
            conn.commit()

            return "<script>alert('글을 수정하였습니다');document.location.href='/board/list'</script>"
        return "<script>alert('비밀번호가 틀렸습니다');history.back();</script>"


####### 글 삭제 #########
@app.route('/board/del/<int:id>')
def del1(id):
    sql = f"select * from board where id={id}"
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    return render_template('board/del.html', rows=rows[0])


@app.route('/board/delok', methods = ["GET","POST"])
def delok():
    if request.method == "POST":
        id = request.form['idx']
        pw = request.form['pass']

        sql = f"select * from board where id={id}"
        cur.execute(sql)
        rows = cur.fetchall()

        if pw ==rows[0][7]:
            sql = f"delete from board where id= {id}"
            cur.execute(sql)
            conn.commit()
            return "<script>alert('글을 삭제하였습니다');document.location.href='/board/list'</script>"
        return "<script>alert('비밀번호가 일치하지 않습니다');history.back();</script>"

if __name__ == "__main__":
    # app.run(host="localhost",port="8200",debug=True)
    app.run()