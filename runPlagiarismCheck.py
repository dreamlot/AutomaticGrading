# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:19:16 2020

1. Go to the assignment directory at 'sourcepath'. 
2. Enter every folder. compare <assignmentname>.py.
3. If plagiarism is detected, log it.

@author: ningyu
"""

import os
from os.path import isfile, join

import filecmp


def checkAll(sourcepath,assignmentname,logfile=None):
	'''
	1
	'''
	# get all folders
	folders= [f for f in os.listdir(sourcepath) if not isfile(join(sourcepath, f))]

	'''
	2 3
	'''
	counter = 0
	for ite1 in folders:
		for ite2 in folders:
			if ite1 != ite2:
				file1 = sourcepath + '/' + ite1 + '/' + assignmentname
				file2 = sourcepath + '/' + ite2 + '/' + assignmentname
				if filecmp.cmp(file1, file2, shallow=True):
					counter += 1
					print(str(counter),ite1,', ',ite2)
					if logfile:
						f = open(logfile,'a')
						f.write(str(counter)+'\n')
						f.write(ite1+'\n')
						f.write(ite2+'\n\n')
						f.close()
	return
                
if __name__ == '__main__': 

	'''
	# Set working directory. 
	# Leave it unchanged if this file is copied to the directory containing all submissions.
	'''
	sourcepath = os.getcwd()
	targetpath = '.'
	targetpath = sourcepath + '/' + targetpath

	logfile= targetpath+'/plagiarism.txt'

	'''
	# Set assignment name.
	# Default name is "assignment.py"
	'''
	assignmentname = "assignment.py"
	
	'''
	# Run.
	'''
	checkAll(sourcepath,assignmentname,logfile)