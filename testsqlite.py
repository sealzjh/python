#!/usr/bin/python
#SQLite test
import sqlite3

conn = sqlite3.connect('newhome')

conn.execute("create table if not exists loupan(loupan_id integer primary key autoincrement,loupan_name varchar(255),num int(11) default 0)")

conn.execute("insert into loupan (loupan_name , num) values ('aaa', 1)")
conn.execute("insert into loupan (loupan_name , num) values ('bbb',2)")

conn.commit()
cur = conn.cursor()

cur.execute("select * from loupan")
res = cur.fetchall()
for row in res:
    print row

cur.close()
conn.close()