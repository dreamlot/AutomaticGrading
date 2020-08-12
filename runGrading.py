# -*- coding: utf-8 -*-
"""
1. Go to the assignment directory at 'sourcepath'. 
2. Enter every folder. Run grade.py.
3. Collect the output.
4. Write the collected data into an Excel file at 'targetpath'

Created on Fri Aug  7 10:53:11 2020

@author: Ningyu Wang
"""
import os
from os.path import isfile, join
from shutil import copyfile

import pandas as pd

'''
# Set working directory. 
# Leave it unchanged if this file is copied to the directory containing all submissions.
'''
sourcepath = os.getcwd()
targetpath = '.'
targetpath = sourcepath + '/' + targetpath


logfile = sourcepath+'/log.xls'

df = pd.DataFrame({
    "Student":[],
    "correctanswer":[],
    "wronganswer":[],
    "grade":[]})

def countCorrectWrong(f,name):
    CORRECT = 0;
    WRONG = 0;
    try:
        for line in f:
            if line[0] == '=':
                break
            elif line[-2] == 'k':
                CORRECT += 1;
            elif line[-2] == 'R':
                WRONG += 1;
    except IndexError:
        pass            
     
    appdf = pd.DataFrame({
        "Student":[name],
        "correctanswer":[CORRECT],
        "wronganswer":[WRONG],
        "grade":[CORRECT/(CORRECT+WRONG)]})
    
    return appdf


'''
1
'''
# get all folders
folders= [f for f in os.listdir(sourcepath) if not isfile(join(sourcepath, f))]


'''
2 3
'''

for ite in folders:
    # copy the grading script to the subfolder
    copyfile(sourcepath+'/'+'grade.py',sourcepath+'/'+ite+'/grade.py')
    
    # do grading
    os.chdir(sourcepath+'/'+ite)
    os.system('python grade.py')
    
    # collect data 
    with open('grading.out','r') as f:
        df = df.append(countCorrectWrong(f,ite))
        

'''
4
'''
# write grades to file
os.chdir(sourcepath)
df.to_excel('gradebook.xlsx')