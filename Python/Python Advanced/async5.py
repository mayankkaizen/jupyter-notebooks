
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(3, 'hello')
    await say_after(4, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

#This is merely an example of asyncio, coroutine function and async, await keywords. 
#This is NOT an example of concurrency. The 2 runs of say_after are not concurrent. 
