This program is created for grading PGE 310 assignments.
The assignments should be in the following structure:
	Each student's submission should be in a single folder named after the student.
	All these folders should be placed in the same directory.
	
Then, copy the three *.py files into the directory containing the folders.
Adjust the grade.py file for each assignemt.
	1. Adjust the assignment file name in line 12.
	2. Adjust the functions to be tested from line 23

The runGrading.py file generates an excel file named 'gradbook.xlsx' which contains all the grading info.

The runPlagiarismCheck.py file generates a txt file named 'Plagiarism.txt' which contains all the duplicated submission.

Warning: The plagiarism checking only detects identical file submission. Adding one space is enough to bypath this detection.

Author: Ningyu Wang