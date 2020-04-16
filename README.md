# Homework Assignment 17

[![Build Status](https://travis-ci.com/PGE383-HPC/assignment17.svg?token=SnMGq692xXXqxzyE6QSj&branch=master)](https://travis-ci.com/PGE383-HPC/assignment17)

When input data is too large to fit into memory on a single node, it's common to partition and/or store it in a collection of smaller 
files that can be processed in parallel.  In this repository, you will find four files `ss.0.0.dat`, `ss.0.1.dat`, `ss.0.2.dat`, `ss.0.3.dat`.  These
files each contain one-forth of the stress-strain curve that we manipulated in [Assignment 7](https://github.com/PGE383-HPC-Students/assignment7). 

Your task in this assignment is to read in the data in parallel from the files, then create an `Epetra.Map` and associated `Epetra.Vector` to store the data.  
Assign the `Epetra.Vector` to a class member variable called `stress`.  Use the `Epetra.Copy` argument for robustness when instantiating the `Epetra.Vector` class.  Once the data is stored in an `Epetra.Vector` is can easily be queried for its overall maximum value using the class function `MaxValue()`.  


## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line:

```bash
mpiexec -np 4 python test.py
```
