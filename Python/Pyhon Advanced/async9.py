
import asyncio

async def longwait(n):
    print('doing long wait')
    await asyncio.sleep(n)

async def main():
    long_task = asyncio.create_task(longwait(10))
    
    try:
        result = await asyncio.wait_for(long_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Got a timeout!')
        print(f'Was the task cancelled? {long_task.cancelled()}')

asyncio.run(main())    
    
