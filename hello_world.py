from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


X = np.random.randint(low=0,high=10,size=4)

print("MPI rank %d of %d processes has X: "%(rank,size),X)
