import asyncio

from async_examples.delay import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)
    
asyncio.run(main())