#!/usr/bin/python


import os
import sys
from diff_file_data import *


#display the options to select the required drivers
# /option_name[]: array containing name of the files
# /list_length: length of array option_name


def disp(list_length):
	print 'Select the driver'
	for num in range(0,list_length):
		print '%s' % option_name[num]


#Reading input from the user
# /user_input: input by user


def inp(list_length):
	user_input = int(input("Enter a choice: "))
	if user_input >=1 and user_input<=list_length: 
		return user_input-1
	else:
		print 'Invalid Choice'
		sys.exit(0)


#depending on the user choice the elements from the list are selected
# /file_path[]: array of paths of the selected drivers
# /list_length: number of pair of files that can be compared
#function_to_display_the_choices
# /required_file: the required driver files which have to be compared
# /shell_command: return command for shell execution


def select(user_input, list_length,temp,option_name):
	file_path=fil[user_input]
	file_cmp=file_path[0]
	files=file_cmp[0]
	first_file=files[0]
	second_file=files[1]
	file_name=option_name[user_input]
	return_statement=command_line_statement(first_file,second_file,file_name)
	call(return_statement)
	return file_name
	for num in (0,len(file_path)):
		if file_path[(2*num)+1]==1:
			file_cmp=file_path[(num+1)*2]
			files=file_cmp[0]
			first_file=files[0]
			second_file=files[1]
			return_statement=command_line_statement(first_file,second_file,temp)
			call(return_statement)
			con_catenate(temp)
		else:
			pass


#function to get the string to be used as shell commmand  
# /first_file: input file 1
# /second_file: input file 2
# /required_file: output diff file 
# /returns: return value of diff


def command_line_statement(first_file,second_file,required_file):
	return ('diff %s %s > %s.txt') % (first_file,second_file,required_file)


#to run the command in shell we use os.system
# /return_statement: return command for shell execution


def call(return_statement):
	os.system(return_statement)


#concatanate multiple diff_files generated
# /file_name: name of the final diff file


def con_catenate(file_name):
	statement=('cat temp.txt >> %s.txt') % file_name
	os.system(statement) 


#open the diff file or display the error element


def file_display(req_file):
	if req_file==-1:
		print 'invalid choice'
		pass
	else:
		shell_command= 'gvim %s.txt' %req_file
		os.system(shell_command)
	

#set variables to zero
# /usip: user input to select the file
# /ret: return statement generated
# /req: required file name 
# /ret: return value of diff
# /name: length of array option_name
# /path: length of array file_path


usip=0

ret=0

t='temp'

req=0

name=len(option_name)

path=len(fil)


disp(name)

usip=inp(name)

ret=select(usip,path,t,option_name)

file_display(ret)
