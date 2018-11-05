'''
Python Standard Library Documentation Recommender (PDR)
	Plugin for Sublime Text 3

Written for: 	University of Lethbridge, CPSC 4210/5210/7210
				Recommendation Systems in Software Engineering
				Project Due: November 29, 2018

Written by:		Justin Petluk
				Lance Chisholm
				Roddy MacCrimmon
				Sean Herridge-Berry
				Matthew Davison
'''

#import modules

#import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by) 


import sublime
import sublime_plugin

import subprocess


import os

print("Current Working Direcotry: " + os.getcwd())
try:
	os.chdir("./PDR")
	print("Changing to: " + os.getcwd())
except:
	print("Already in PDR")



class ipdrCommand(sublime_plugin.TextCommand):

	def line_next(self,pos):
		return self.view.line(pos)[1]+1

	def line_prev(self,pos):
		return self.view.line(pos)[0]-1

	def run(self, view):
		#PDRcommand = "C:/Users/legom/Documents/GitHub/PDR"
		PDRcommand = "./main.py"

		
		#get a random number


		#declare things
		comment_list = []
		comment_block = []
		flag = False

		#get the current buffer's file name
		filename = self.view.file_name()

		#open the file and read each line
		with open(filename) as f:
			lines = f.readlines()

		#obtain the position of the cursor, returning the line number of where
		#the cursor is
		pos = self.view.sel()[0].begin()
		cursor_line = self.view.rowcol(pos)[0]
		#print(cursor_line)
		#print(self.view.line(pos))
		line = lines[cursor_line]
		line = line.replace("\t", "")

		
		#self.view.show_popup("hello there",1, 1, 10, 10, self.view.hide_popup())
		#if (line.find("#", 0, 1) == 0):
		line = line.replace("\t", "")
		line = line.replace("\n", "")
		line = line.replace("#", "")
			
		try:
			unproc = subprocess.check_output(["python", PDRcommand, line])

			print(unproc)
			output = ""
			for char in range(0,len(unproc)):
				if chr(unproc[char]) is "$":
					output = output + "<br>"
				else:
					output = output + chr(unproc[char])
		except:
			output = "Please enter plain sentence without special chars"
 
		self.view.show_popup(output,1, -1, 1000, 1000, self.view.hide_popup())
		#print(subprocess.check_output(["python", PDRcommand, line]))
		

		#output = subprocess.Popen(PDRcommand, shell = True)
		#subprocess.check_output("python ./PDR/main.py")
		#in each line, checkr ''' and #
		#for line in lines:
		#	line = line.replace("\t", "")
		#	line = line.replace("\n", "")
		#	if (line.find("#", 0, 1) == 0):
		#		comment = line[1:len(line)]
		#		comment_list.append(comment)

		#for line in lines:
		#	if (line.find("'''") == 0 and flag == False):
		#		flag = True
		#	elif (line.find("'''") == 0 and flag == True):
		#		flag = False
		#	if flag == True:
		#		line = line.replace("\'\'\'","")
		#		line = line.replace("\t", "")
		#		line = line.replace("\n", "")
		#		if (line != ""):
		#			comment_block.append(line)

#check for ''' (start of multiline comment block)
	#continue to read lines until another ''' occurs
	#save lines to a string

#check for # (start of single line comment)
	#save line to a string

#strip comment markers and newline characters

#safely close file

#run the resulting comment to Lance's function (RETURN A SINGLE STRING TO RUN THROUGH LANCE'S THING)
