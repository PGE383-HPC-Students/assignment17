#!/usr/bin/env python
import os
import unittest
from PyTrilinos import Epetra

from assignment15 import Max

class TestMax(unittest.TestCase):

    def setUp(self):

        comm = Epetra.PyComm()
        self.T = Max('ss', comm)
    
    def tearDown(self):

        self.T.comm.Barrier()

    def test_max(self):

        max_value = self.T.get_max()

        self.assertAlmostEqual(toughness, 150571.37930620485, 2)


if __name__ == '__main__':
    unittest.main()
