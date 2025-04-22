import asyncio

from delay import delay


async def main():
    delay_task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача выполняется дольше обычного...")
        result = await delay_task
        print(result)


asyncio.run(main())
