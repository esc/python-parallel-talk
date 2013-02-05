import multiprocessing as mp

def compute(arg, lock):
    lock.acquire()
    arg.value += 10

arg = mp.Value('d', 0.0)  # synchronized shared object, type double
lock = mp.Lock()          # non-recursive lock object

p1 = mp.Process(target=compute, args=(arg, lock))
p2 = mp.Process(target=compute, args=(arg, lock))
p1.start()
p2.start()
p1.join()
