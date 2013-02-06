from MPI_Import import mpi_import, MPI
with mpi_import():
    import os
    import re
    import math
    import decimal
    import optparse
    import platform
    import string
    import zipfile
    import numpy

comm = MPI.COMM_WORLD
rank, size = comm.Get_rank(), comm.Get_size()
print "Hello World! I am rank %d of size %d"  % (rank, size)
