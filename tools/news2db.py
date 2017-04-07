# -*- coding: utf-8 -*- 
#!/usr/bin/python
import json
import re
import sqlite3
import sys
import Global
reload(sys)
sys.setdefaultencoding('utf-8')

file = open(Global.content_dir)
conn = sqlite3.connect(Global.db_dir)
insertsql = "create table if not exists news(url text primary key,title text,time text,summary text,content text)"
print insertsql
conn.execute(insertsql)
conn.commit()

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
	insertsql = "replace into news(url,title,time,summary) values ('"+str(data['url']).decode('utf-8')+"','"+str(data['title']).decode('utf-8')+"','"+str(data['time']).decode('utf-8')+"','"+str(datacontent).decode('utf-8')+"')"
	#print insertsql
	conn.execute(insertsql)
	conn.commit()

conn.close()
