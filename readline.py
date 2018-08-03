#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This is a interface to extract few lines ahead of an extreme big file
# Paremeters:
# 1. start: where the extracting started
# 2. lineNum: how many lines to extract
# 3. file_path: the origin big file

import os

lineNum = 100
print('Input the file or directory path:  ')
file_path = raw_input()

def set_new_file(old_file):
	if old_file.find('.') == -1:
		new_file = old_file + '_few_lines'
	else:
		file_name = old_file.split('.')[0]
		file_type = old_file.split('.')[1]
		new_file = file_name + '_few_lines.' + file_type
	return new_file

def extract_lines(old_file, new_file):
	r_file = open(old_file, 'r')
	w_file = open(new_file, 'w')
	for i in range(lineNum):
		few_line = r_file.readline()
		w_file.write(few_line)
	r_file.close()

def get_lineNum(file_path):
	file = open(file_path, 'r')
	count = -1
	for count,line in enumerate(file):
		pass
		count +=1
	return count

def set_lineNum_for_file(file_path):
	print 'There are ' + str(get_lineNum(file_path)) + ' lines in the file.'
	lineNum = int(raw_input("how many lines to extract: "))

if os.path.isdir(file_path):
	path = os.path.abspath('.') + '/' + file_path
	dirs = os.listdir(path)
	new_dirs = path + '/' + "few_lines/"
	if not os.path.exists(new_dirs):
		os.makedirs(new_dirs)
	for file in dirs:
		file_path = path + '/' + file
		set_lineNum_for_file(file_path)
		extract_lines(file_path, new_dirs + set_new_file(file))
else:
	set_lineNum_for_file(file_path)
	extract_lines(file_path, set_new_file(file_path))

