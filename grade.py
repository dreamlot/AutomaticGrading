#!/usr/bin/env python
import sys
import unittest

from unittest.mock import MagicMock

import nbconvert

import numpy as np

import os.path 

if os.path.isfile('assignment.ipynb'):
    with open("assignment.ipynb") as f:
        exporter = nbconvert.PythonExporter()
        python_file, _ = exporter.from_file(f)
    
    with open("assignment.py", "w") as f:
        f.write(python_file)

from assignment import *

def func_text(x):
	return(np.sin(x-1))

def func_g(x):
	return(x-np.sin(x-1))

class TestSolution(unittest.TestCase):
		
	
	def test_func1a(self):
		np.testing.assert_array_almost_equal(func1a(func_text,0.5,1.5),[1,0],decimal = 2)
		
	def test_func1b(self):
		np.testing.assert_array_almost_equal(func1b(f,1,10),[1.393662452697754, 8.58306884765625e-06],decimal = 2)
	
	def test_func2a(self):
		np.testing.assert_array_almost_equal(func2a(func_text,0.5,1.5),[1,0],decimal = 2)
		
	def test_func2b(self):
		np.testing.assert_array_almost_equal(func2b(f,1,10),[1.393671561938863, 4.321129150941516e-06],decimal = 2)
    
	def test_func3a(self):
		np.testing.assert_array_almost_equal(func3a(func_g,1.1),[1,0],decimal = 2)
		
	def test_func3b(self):
		np.testing.assert_array_almost_equal(func3b(g,1),[1.393662452697754, 5.119836595739946e-06],decimal = 2)
	
	
	def test_func4a(self):
		np.testing.assert_array_almost_equal(func4(),[159.7140640504605,3805.5014021736324,3805.4930398282045],decimal = 0)
		
	def test_func4b(self):
		np.testing.assert_array_almost_equal(func4(),[159.7140640504605,3805.5014021736324,3805.4930398282045],decimal = 0)
		

def main(out = sys.stderr, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
      
if __name__ == '__main__': 
    with open('grading.out', 'w') as fout: 
        main(fout) 
