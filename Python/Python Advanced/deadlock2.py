
import concurrent.futures as conf

def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())

executor = conf.ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)
