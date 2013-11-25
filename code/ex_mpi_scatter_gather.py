from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 4
# rank 0 should send the message
if comm.rank == 0:
    msg = numpy.arange(N, dtype=int)
else:
    msg = None

# dest should hold the scattered message
dest = numpy.empty(N/comm.size, dtype=int)
# ans should hold the gathered result
ans = numpy.empty(comm.size, dtype=int)

# scatter the array
comm.Scatter([msg, MPI.INT],
             [dest, MPI.INT], root=0)

# do the work
mysum = numpy.sum(dest)

# gather the result
comm.Gather([mysum, MPI.INT],
            [ans, MPI.INT], root=0)
