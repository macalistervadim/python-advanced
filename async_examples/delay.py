import asyncio

from async_timed import async_timed


@async_timed()
async def delay(delay_seconds) -> int:
    print(f"Delaying {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"Finished delaying {delay_seconds} seconds")
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(5))
    task_two = asyncio.create_task(delay(8))

    await task_one
    await task_two


asyncio.run(main())
