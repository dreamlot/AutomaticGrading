This program is created to automatically grade the Python assignments on Github Classroom. It works on a local computer to grade the downloaded assignments. It can also grade assignments stored in the same structure:

This program is created for grading PGE 310 assignments.
The assignments should be in the following structure:
	Each student's submission should be in a single folder named after the student.
	All these folders should be placed in the same directory.
	
Then, copy the two *.py files into the directory containing the folders.

Adjust the grade.py file for your assignment.

The runGrading.py file generates an excel file named 'gradbook.xlsx' which contains all the grading info.

It is recommanded to modify or remove several checks in the grade.py file and distribute it to the students to grant them the chance to verify if their assignment works. This grading machine records zero grade for submitted Python files with syntax error.


The workflow of this system was initially created by Dr. John Foster, a Professor at The University of Texas at Austin. This program utilizes the idea and is thus an offspring.

Author: Ningyu Wang
