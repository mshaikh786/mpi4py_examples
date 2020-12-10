from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

X = np.empty(4,dtype='i')
if rank==0:
	X = np.random.randint(low=0,high=10,size=4,dtype='i')

comm.Bcast(X, root=0)

print("MPI rank %d of %d processes has X: "%(rank,size),X)
