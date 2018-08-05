'''
	Usage: store txt to sql

	Example: txt format (split by '\t') @line30
		id 	name
		01	aaa
		02	bbb
		03	ccc

	PS: 
		1. MySQLdb should be installed way like pip install
		2. .txt and .py should be put int the same dir or you can set the correct filepath
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

file_name = 'mid2name_new.txt'
table_name = 'mid2name'

def get_tuple_list_from_file(file):
	f2read = open(file, 'r')
	tuple_list = []
	for line in f2read.readlines():
		line = line.strip()
		if not len(line):
			continue
		mid = line.split('\t', 1)[0]
		name = line.split('\t', 1)[-1]
		column = (mid, name)
		tuple_list.append(column)
	f2read.close()
	return tuple_list

def insert_data2table(table):
	try:
		password = '22kon'
		connect = MySQLdb.connect(host='localhost',user='root',passwd=password,db='OpenNRE',port=3306)
		cursor = connect.cursor()

		tuple_list = get_tuple_list_from_file(file_name)
		create_sql = "CREATE TABLE %s (id VARCHAR(20), name VARCHAR(255), PRIMARY KEY(id))" %(table)
		print 'check create sql:' + create_sql
		cursor.execute(create_sql)

		test_insert_sql = "INSERT IGNORE INTO %s (id, name) VALUES ('%s', '%s')" %(table, tuple_list[0][0], tuple_list[0][1])
		print 'check insert sql:' + test_insert_sql

		for id2name in tuple_list:
			insert_sql = "INSERT IGNORE INTO %s (id, name) VALUES ('%s', '%s')" %(table, id2name[0], id2name[1])
			cursor.execute(insert_sql)

		connect.commit()
		cursor.close()

	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		connect.rollback()

	finally:
		connect.close()

insert_data2table(table_name)