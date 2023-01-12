
#single thread example

import os
import threading

print(f'python process running with process id: {os.getpid()}')

total_t = threading.active_count()
thread_n = threading.current_thread().name

print(f'python is currently running {total_t} thread(s)')
print(f'The current thread is {thread_n}')
