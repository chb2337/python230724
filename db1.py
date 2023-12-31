# db1.py
import sqlite3

#연결객체 생성
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("create table if not exists PhoneBook" +
    " (id integer primary key autoincrement, " +
    " name text, phoneNum text);")

#1건입력
cur.execute("insert into PhoneBook (name, phoneNum) values " +
    " ('홍길동', '010-111');")

#입력파라메터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values " +
    " (?,?);", (name, phoneNumber))

#다중의 행을 입력
datalist = (("이순신", "010-333"), ("박문수", "010-123"))
cur.executemany("insert into PhoneBook (name, phoneNum) values " +
    " (?,?);", datalist)


#검색구문
cur.execute("select * from PhoneBook;")
print("---fetchone()---") #버퍼에서 레코드 삭제됨
print(cur.fetchone())
print("---fetchone()---") #버퍼에서 레코드 삭제됨
print(cur.fetchone())
print("---fetchone(2)---")
print(cur.fetchmany(2))
cur.execute("select * from PhoneBook;") # 버퍼 다시 채우기
print("---fetchall()---")
print(cur.fetchall())



# for row in cur:
#     print(row)
