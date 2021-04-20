#!/usr/bin/env python
import numpy as np

from PyTrilinos import Epetra

class Max():

    def __init__(self, basename, comm):

        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()


    def get_max(self):

        return #maximum value across all procs




if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    T = Max('ss', comm)

    print(T.get_max())
