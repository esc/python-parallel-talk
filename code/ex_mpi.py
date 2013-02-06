from mpi4py import MPI
comm = MPI.COMM_WORLD
print "Hello from %s, %d of %d"\
    % (MPI.Get_processor_name(),
    comm.rank, comm.size)
