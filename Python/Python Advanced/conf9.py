
from concurrent import futures
import os


def task(n):
    return (n, os.getpid())

def main():
    ex = futures.ProcessPoolExecutor(max_workers=2)
    results = ex.map(task, range(5, 0, -1))

    for n, pid in results:
        print('ran task {} in process {}'.format(n, pid))
        
if __name__ == '__main__':
    main()        