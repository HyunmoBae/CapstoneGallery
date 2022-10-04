import pymysql

#데이터베이스 연결
conn = pymysql.connect(host='localhost',
                        user='root',
                        password='autoset',
                        db='dcu',
                        charset='UTF8')

curs = conn.cursor(pymysql.cursors.DictCursor) #딕셔너리 형태로 결과를 반환 판다스로 데이터프레임 형태로 

#테이블 생성
# sql = ''' create table board (
#     id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     title varchar(100),
#     name varchar(100),
#     memo text,
#     email varchar(100),
#     wdate varchar(100),
#     hit int(11),
#     pw varchar(100)
#     )
#     '''

# conn.execute(sql)
# conn.commit()
# conn.close()

#데이터 삽입
# sql = "insert into user (name,email,phone) values (%s,%s,%s)"

# curs.execute(sql,("bhm","tsi0520@naver.com","010-1234-6789"))
# curs.execute(sql,("abc","tss0520@ddver.com","010-0004-6789"))
# curs.execute(sql,("dem","tse0520@aaver.com","010-1111-6789"))
# curs.execute(sql,("rem","tse0523@aaver.com","010-2222-6789"))
# curs.execute(sql,("tem","tse0524@aaver.com","010-4444-6789"))

# conn.commit()
# conn.close()

#글을 불러내기
# sql = "select * from user order by name"

#명령실행
# curs.execute(sql)
# rows = curs.fetchmany(5)
# print(rows)
# conn.close()

#글 수정
# sql = "update user set phone = %s where name = %s"
# curs.execute(sql,('폰없음','abc'))
# conn.commit()
# conn.close()

#글 삭제
# sql = "delete from user where id = %s"
# curs.execute(sql,(8))
# conn.commit()
# conn.close()

#연결 닫기
# for data in curs:
#     print(data) 