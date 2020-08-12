#!/usr/bin/env python
import sys
import unittest

from unittest.mock import MagicMock

import nbconvert

import numpy as np


with open("assignment.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment.py", "w") as f:
    f.write(python_file)

from assignment import IterativeSolver


class TestSolution(unittest.TestCase):


    def test_solver(self):
        A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
        b = np.array([1, 2, 3])
        solver = IterativeSolver(A, b)
        np.testing.assert_array_almost_equal(solver.gauss_seidel_solve(), np.array([2.5, 4., 3.5]), decimal=6)
		
    def test_solvers2(self):
        A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
        b = np.array([1, 2, 3])
        solver = IterativeSolver(A, b)
        np.testing.assert_array_almost_equal(solver.additionaltest(1),np.array([0.1,0.2,0.3]),decimal=6)
		
    def test_solvers3(self):
        A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
        b = np.array([1, 2, 3])
        solver = IterativeSolver(A, b)
        np.testing.assert_array_almost_equal(solver.additionaltest(2),np.array([0.1,0.2,0.4]),decimal=6)
		
    def test_solvers4(self):
        A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
        b = np.array([1, 2, 3])
        solver = IterativeSolver(A, b)
        np.testing.assert_array_almost_equal(solver.additionaltest(2),np.array([0.1,0.3,0.4]),decimal=6)


def main(out = sys.stderr, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
      
if __name__ == '__main__': 
    with open('grading.out', 'w') as f: 
        main(f) 
