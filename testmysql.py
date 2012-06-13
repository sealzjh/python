#!/usr/bin/python
#Filename: testmysql.py
import MySQLdb
conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='cnwgo');
cursor = conn.cursor();

sql = "SELECT * FROM user LIMIT 1";
count = cursor.execute(sql)
row = cursor.fetchone()

print row[1];

cursor.close();
