import asyncio
import aiohttp

async def get():
    async with aiohttp.ClientSession() as s:
        resp = await s.request('GET', '')
        # print(resp._closed)
        # print(resp._connection)
        # print(resp._released)
        c = await resp.text()
        print()
    print(resp.closed)
    # print(resp.connection)
    # print(resp._released)
    # return c

c = asyncio.run(get())