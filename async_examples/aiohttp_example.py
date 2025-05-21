import asyncio
import aiohttp
from aiohttp import ClientSession

from async_timed import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=10)
    async with session.get(url, ssl=False, timeout=ten_millis) as response:
        return response.status
    
    
@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=10, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        urls = ["https://example.com" for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*requests)
        print(status_code)
        
asyncio.run(main())