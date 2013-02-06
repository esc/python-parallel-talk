import ctypes
from multiprocessing import sharedctypes, Process
import numpy
from numpy import ctypeslib

def f(cta):
    from numpy import ctypeslib
    npa = ctypeslib.as_array(cta._obj)
    npa[0] = npa.sum()

cta = sharedctypes.Array(ctypes.c_double, numpy.arange(1e6))
npa = ctypeslib.as_array(cta._obj)
p1 = Process(target=f, args=(cta,))
