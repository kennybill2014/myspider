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
	data = json.loads(line)
	content = ''
	for item in data['content']:
		if content == '':
			content = item;
		else:
			content = content + '&#$' + item
	insertsql = "replace into news(url,title,time,summary,content) values ('"+str(data['url']).decode('utf-8')+"','"+str(data['title']).decode('utf-8')+"','"+str(data['time']).decode('utf-8')+"','"+str(data['summary']).decode('utf-8')+"','"+content.decode('utf-8')+"')"
	print insertsql
	conn.execute(insertsql)
	conn.commit()

conn.close()
