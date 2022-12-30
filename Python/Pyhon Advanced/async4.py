
import asyncio

async def inner():
    await asyncio.sleep(5)
    print("running inner")
    return 1

async def outer():
    print("running outer")
    await inner()
    print("Done")
    
asyncio.run(outer())    
