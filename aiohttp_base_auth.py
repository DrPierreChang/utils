import json

import aiohttp
import asyncio


url = ''
user= ''
password = ''



async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(url, auth=aiohttp.BasicAuth(user, password)) as resp:
            print(resp.status)
            print(resp.text)


asyncio.run(main())
