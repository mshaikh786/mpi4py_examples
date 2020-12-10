import numpy
import mpi4py.MPI as MPI
def Serial_dot(x,y,n):
 sum = 0.0
 for i in xrange(0,n):
 	sum = sum + x[i]*y[i]
 return sum
vec1 = numpy.ones(100, 'd')
vec2 = numpy.ones(100, 'd')
my_rank = MPI.COMM_WORLD.Get_rank()
p = MPI.COMM_WORLD.Get_size()
n_bar = int(len(vec1)/p)
my_start = my_rank*n_bar
my_end = (my_rank+1)*n_bar
local_x = vec1[my_start:my_end]
local_y = vec2[my_start:my_end]
dot = 0.0
local_dot = Serial_dot(local_x, local_y, n_bar)
dot = MPI.COMM_WORLD.Reduce(local_dot, None, MPI.SUM, 0)
if (my_rank == 0):
 print ("Dot Product completed: product = %f" % dot)
