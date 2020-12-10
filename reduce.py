from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


X = np.empty(1,dtype='i')
x = np.random.randint(low=0,high=10,size=1,dtype='i')
print("MPI rank %d of %d processes has in x:" %(rank,size),x)



comm.Reduce(x,X, op=MPI.SUM,root=0)
if rank == 0: 
	print("MPI rank %d of %d processes has in X:" %(rank,size),X)
