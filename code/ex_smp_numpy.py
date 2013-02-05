import ctypes
import numpy
from multiprocessing import sharedctypes, Process

def f(a):
   from numpy import ctypeslib
   nd_a = ctypeslib.as_array(a)
   nd_a[0] = numpy.sum(a)

npa = numpy.linspace(1, 1e7)
cta = sharedctypes.Array(ctypes.c_double, npa)
p = Process(target=f, args=(cta,))

