import multiprocessing as mp
import time
import random

def mult(arg):
    time.sleep(random.uniform(1,5))
    arg.value *= 10

def add(arg):
    time.sleep(random.uniform(1,5))
    arg.value += 10

arg = mp.Value('d', 0.0)  # synchronized shared object, type double

p1 = mp.Process(target=mult, args=(arg,))
p2 = mp.Process(target=add, args=(arg,))
p1.start(); p2.start(); p1.join(); p2.join()
print arg.value
