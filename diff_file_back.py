#!/usr/bin/python

import os
from test_data import *

#function_to_display_the_choices
# /required_file: the required driver files which have to be compared
# /shell_command: return command for shell execution

def file_display(required_file):
	shell_command= 'gvim %s.txt' %required_file
	os.system(shell_command)
	
#display the options to select the required drivers
# /d[]: name of the files

def disp():
	print 'Select the driver'
	print '%s' % d[0]
	print '%s' % d[1]
	print '%s' % d[2]
	print '%s' % d[3]
	print '%s' % d[4]

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

#Reading input from the user
# /user_input: input by user

def inp():
	user_input = int(input("Enter a choice: "))
	return user_input

#depending on the user choice the elements from the list are selected
# /l[]: path of the selected drivers

def select(user_input,required_file):
	if user_input==1:
		first_file=l[0]
		second_file=l[1]
		return_statement=command_line_statement(first_file,second_file,required_file)
		return return_statement
	elif user_input==2:
		first_file=l[2]
		second_file=l[3]
		return_statement=command_line_statement(first_file,second_file,required_file)
		return return_statement
	elif user_input==3:
		first_file=l[6]
		second_file=l[7]
		return_statement=command_line_statement(first_file,second_file,required_file)
		return return_statement
	elif user_input==4:
		first_file=l[8]
		second_file=l[9]
		return_statement=command_line_statement(first_file,second_file,required_file)
		return return_statement
	elif user_input==5:
		first_file=l[10]
		second_file=l[11]
		return_statement=command_line_statement(first_file,second_file,required_file)
		return return_statement
	else:
		return_statement=0 
		return return_statement


#set variables to zero

# /usip: user input to select the file
# /ret: return statement generated
# /req: required file name 
# /ret: return value of diff

usip=0
ret=0

disp()

usip=inp()

req=d[usip-1]

ret=select(usip,req)

if ret==0:
	print 'Invalid choice'
else:
	call(ret)

#there are two set of files to be compared so the diff between the second set is is determined using the following 

if usip==2:
	first_file=l[4]
	second_file=l[5]
	return_statement=command_line_statement(first_file,second_file,6)
	call(return_statement)
	call('cat %s.txt 6.txt') %req
	
else:
	pass

file_display(req)
