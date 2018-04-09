#!/usr/bin/env python
import numpy as np

from PyTrilinos import Epetra

class Max():

    def __init__(self, basename, comm):

        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

        self.load_data(basename)


    def load_data(self, basename):

        my_data = np.loadtxt(basename + '.' + str(self.rank) + '.' + str(self.size) + '.dat')

        my_stress = my_data[:,1]

        my_length = my_stress.shape[0]

        standard_map = Epetra.Map(-1, my_length, 0, self.comm)

        self.stress = Epetra.Vector(Epetra.View, standard_map, my_stress)


    def get_max(self):

        return self.stress.MaxValue()[0]




if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    T = Max('ss', comm)

    print(T.get_max())
