
import asyncio

async def longwait(n):
    print('doing long wait')
    await asyncio.sleep(n)

async def main():
    long_task = asyncio.create_task(longwait(10))
    
    try:
        result = await asyncio.wait_for(asyncio.shield(long_task), timeout=13)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Taking longer than usual. Please wait.')
        #result  = await long_task   #why not use the result from try block?
        print(result)

asyncio.run(main())    
    
