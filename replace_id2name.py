import MySQLdb

file_name = 'freebase_mtr100_mte100-valid.txt'
connect = MySQLdb.connect(host='localhost',user='root',passwd='22kon',db='OpenNRE',port=3306)	

def get_name_from_id(mid):
	try:
		cursor = connect.cursor()
		select_sql = "SELECT name FROM mid2name WHERE id='%s';" %(mid)
		# print 'check select sql:' + select_sql
		cursor.execute(select_sql)
		name = cursor.fetchone()
		return name
		connect.commit()
		
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		connect.rollback()
	finally:
		cursor.close()

def replace_id2name(file):
	f2read = open(file, 'r')
	file_len = len(f2read.readlines())
	print 'Here are %d lines in the file. ' %(file_len)
	print 'Read from lineNo __ to lineNo __'
	start = int(input())
	end = int(input())
	f2read.seek(start)
	for line in f2read.readlines(end-start):
		mid_relation_mid = line.strip().split('\t')
		mid = mid_relation_mid[0]
		# since the return of cursor.fetchone() ia a tuple
		name = get_name_from_id(mid)
		if name:
			print name[0]

		
	connect.close()
	f2read.close()

replace_id2name(file_name)