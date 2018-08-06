import MySQLdb

file_name = 'freebase_mtr100_mte100-train.txt' 
connect = MySQLdb.connect(host='localhost',user='root',db='test',port=3306)	

def get_keymids_from_keyword(keyword):
	try:
		cursor = connect.cursor()
		select_sql = "SELECT id FROM mid2name WHERE name='" + "%s"%(keyword) + "';"
		print select_sql
		print "Searching for '%s' ing..."%(keyword)
		cursor.execute(select_sql)
		mids = cursor.fetchall()
		# print 'Here are %d mid for keyword %s :' %(len(mids), keyword)
		return mids
		connect.commit()
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		connect.rollback()
	finally:
		cursor.close()

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

def get_relations_by_keymid(file, keymids):
	f2read = open(file, 'r')
	for line in f2read.readlines():
		for mid in keymids:
			if mid and line.find(mid[0]) == 0:
				mid_relation_mid = line.strip().split('\t')
				mid1 = mid_relation_mid[0]
				mid2 = mid_relation_mid[-1]
				# since the return of cursor.fetchone() ia a tuple
				name1 = get_name_from_id(mid1)
				name2 = get_name_from_id(mid2)
				if name1 and name2:
					entity1 = '<' + name1[0] + '>'
					entity2 = '<' + name2[0] + '>'
					result = line.replace(mid1,entity1).replace(mid2,entity2).strip()
					result = entity1 + '\t' + result.split('/')[-1]
					print result
			else:
				continue
	connect.close()
	f2read.close()
	
def print_names(keymids):
	for mid in keymids:
		names = get_name_from_id(mid[0])
		if names:
			print names[0]
			
keyword = raw_input('Keyword to search: ')
keymids = get_keymids_from_keyword(keyword)
get_relations_by_keymid(file_name, keymids)