
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def power2():
    print('doing power2')
    return 2**100000000

async def main():
    task1 = asyncio.create_task(say_after(3, 'hello'))
    task2 = asyncio.create_task(say_after(4, 'world'))
    task3 = asyncio.create_task(power2())

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task3
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())    
