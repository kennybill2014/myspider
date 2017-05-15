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

conn=MySQLdb.connect(host='localhost',user='root',passwd='ljwsqw20',db='spider',port=8889,unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',charset='utf8')
file = open(Global.content_dir)
cursor = conn.cursor()
insertsql = "select * from totalcount"
result=cursor.execute(insertsql)
#cursor.scroll(0,'absolute')
totalcount = cursor.fetchone()[0]
conn.commit()

while 1:
	line = file.readline()
	if not line:
		break
	line = re.sub("'","’",line)
	#encoded_json = json.dumps(line)
	data = json.loads(line)
	datacontent = str(data['content'])
#	datacontent = str(datacontent).replace("u\'", "\'")
	#datacontent = str(datacontent).replace("\'", "\"")
	#datacontent = datacontent.decode("unicode-escape").encode("utf-8")

	coverlist = str(data['cover'])
	print datacontent
	insertsql = "replace into channel255(id,type,url,title,show_time,introduction,cover,content_type,cover_show_type,publish_time,content,source,group_id) values ('" + str(totalcount) + "','" + str(data['type']) + "','" + str(data['url']).decode('utf-8') + "','" + str(data['title']).decode('utf-8') + "','" + str(data['show_time']).decode('utf-8') + "','" + str(data['introduction']).decode('utf-8') + "','" + coverlist + "','" + str(data['content_type']).decode('utf-8')+"','" + str(data['cover_show_type']).decode('utf-8') + "','" + str(data['publish_time']).decode('utf-8') + "','" + str(datacontent).decode('utf-8') + "','" + str(data['source']).decode('utf-8')+ "','" + str(data['group_id']).decode('utf-8')+ "')"
#	print insertsql
	cursor.execute(insertsql)
	totalcount = totalcount+1
insertsql = "UPDATE totalcount SET count = " + str(totalcount) + " WHERE 1"
result = cursor.execute(insertsql)
cursor.close()
conn.commit()
conn.close()
file.close()
