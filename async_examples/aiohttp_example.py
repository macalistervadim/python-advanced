import asyncio
import aiohttp
from aiohttp import ClientSession

from async_timed import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=.01)
    async with session.get(url, ssl=False, timeout=ten_millis) as response:
        return response.status
    
    
@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url = "https://www.google.com"
        status = await fetch_status(session, url)
        print(f"Status code for {url}: {status}")
        
asyncio.run(main())