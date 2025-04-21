import asyncio


async def delay(delay_seconds) -> int:
    print(f"Delaying {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"Finished delaying {delay_seconds} seconds")
    return delay_seconds
