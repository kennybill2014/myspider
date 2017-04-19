# -*- coding: utf-8 -*- 
#!/usr/bin/python
import json
import re
#import sqlite3
import sys
import Global
import hashlib
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

#conn = MySQLdb.connect("127.0.0.1:8889","root","ljw","news")
#conn=MySQLdb.connect(host='localhost',port = 8889,user='root',passwd='ljw',db ='news')
conn=MySQLdb.connect(host='localhost',user='root',passwd='ljwsqw20',db='spider',port=8889)
cursor = conn.cursor()

file = open(Global.content_dir)
#conn = sqlite3.connect(Global.db_dir)
insertsql = "create table if not exists news(uid VARCHAR(255) NOT NULL PRIMARY KEY ,url text,title text,time text,summary text,content text)"
#print insertsql
cursor.execute(insertsql)
#conn.commit()

while 1:
	line = file.readline()
	if not line:
		break
	line = re.sub("'","’",line)
	#encoded_json = json.dumps(line)
	data = json.loads(line)
	datacontent = str(data['content'])
	datacontent = str(datacontent).replace("u\'", "\'")
	datacontent = str(datacontent).replace("\'", "\"")
	datacontent = datacontent.decode("unicode-escape").encode("utf-8")

	uid = hashlib.md5(str(data['url']).decode('utf-8')).hexdigest()
	insertsql = "replace into news(uid,url,title,time,summary,content) values ('"+str(uid)+"','"+str(data['url']).decode('utf-8')+"','"+str(data['title']).decode('utf-8')+"','"+str(data['time']).decode('utf-8')+"','"+str(data['summary']).decode('utf-8')+"','"+str(datacontent).decode('utf-8')+"')"
	print insertsql
	cursor.execute('set names utf8')
	cursor.execute(insertsql)
cursor.close()
conn.commit()
conn.close()
