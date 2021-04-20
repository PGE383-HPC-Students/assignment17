#!/usr/bin/env python

# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import unittest
from PyTrilinos import Epetra

from assignment17 import Max

class TestMax(unittest.TestCase):

    def setUp(self):

        self.comm = Epetra.PyComm()
        self.comm.Barrier()
        self.T = Max('ss', self.comm)
    
    def tearDown(self):

        self.T.comm.Barrier()

    def test_max(self):

        max_value = self.T.get_max()

        self.assertAlmostEqual(max_value, 158314.35447835593, 2)


if __name__ == '__main__':
    unittest.main()
    exit()
