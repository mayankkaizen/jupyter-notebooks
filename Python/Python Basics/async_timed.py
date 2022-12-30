
import functools
import time

def async_timed():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            print(f'starting {func} with args {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'finished {func} in {total:.4f} second(s)')
        return wrapped
    return wrapper

