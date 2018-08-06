import MySQLdb

file_name = 'person.txt'
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
	print 'Read from lineNo _ to lineNo _ :'
	start = int(input())
	end = int(input())
	f2read.seek(0)
	for line in f2read.readlines()[start:end]:
		mid_relation_mid = line.strip().split('\t')
		mid1 = mid_relation_mid[0]
		mid2 = mid_relation_mid[-1]
		# since the return of cursor.fetchone() ia a tuple
		name1 = get_name_from_id(mid1)
		name2 = get_name_from_id(mid2)
		if name1 and name2:
			entity1 = '<' + name1[0] + '>'
			entity2 = '<' + name2[0] + '>'
			result = line.replace(mid1, entity1).replace(mid2, entity2).strip()
		print result
		
	connect.close()
	f2read.close()

replace_id2name(file_name)