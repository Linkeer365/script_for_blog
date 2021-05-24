import sqlite3
import os
import datetime

history_dir=r"C:\Users\linsi\AppData\Local\CentBrowser\User Data\Default"
history_path=os.path.join(history_dir,"History")

def get_urls(book_type="main"):
	# 数据库操作，得到历史数据中所有的网址
	three_days_before=datetime.datetime.now()-datetime.timedelta(days=3)
	print(three_days_before)
	c=sqlite3.connect(history_path)
	cursor=c.cursor()
	pattern_str='https://library.bz/{}/uploads/new/%'.format(book_type)
	select_statement="SELECT urls.url FROM urls,visits WHERE date(last_visit_time/1000000-11644473600,'unixepoch','localtime')>date('now','-3 days') AND urls.id=visits.url AND urls.url LIKE '{}' ORDER BY last_visit_time LIMIT 5".format(pattern_str)
	# select_statement="SELECT urls.url FROM urls,visits WHERE urls.id=visits.url AND urls.url LIKE '{}' AND datetime('now','-1 day','last_visit_time')>1".format(pattern_str)
	print(select_statement)
	cursor.execute(select_statement)
	results=cursor.fetchall()
	for each in results:
		print(each)
	# print(url)

get_urls()