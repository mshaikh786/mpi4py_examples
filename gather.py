from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

X = np.empty(4,dtype='i')
x = np.random.randint(low=0,high=10,size=1,dtype='i')
print("MPI rank %d of %d processes has gather in x:" %(rank,size),x)

comm.Gather(x,X, root=0)

if rank == 0:
	print("MPI rank %d of %d processes has gather in X:" %(rank,size),X)
