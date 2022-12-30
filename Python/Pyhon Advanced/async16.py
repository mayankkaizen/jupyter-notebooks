
import asyncio

async def main():
    print("Running main")
    await asyncio.sleep(1)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    print("Done!")
    loop.close()
