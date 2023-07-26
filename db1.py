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


#검색구문
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
