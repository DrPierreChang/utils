import asyncio
import encodings
import aiohttp
from aiohttp import web
import json

async def main():
    with open('json_example.json', 'rb') as file:
        async with aiohttp.ClientSession() as session:

            # result = await session.post(
            #     url= "",
            #     data=file.read())
            # print(result.status)

            # send as json
            # test_json = json.dumps(test_json, ensure_ascii=False)
            # print(test_json)
            # print(json.loads(file.read()))


            try:
                5 / 0
                test_json = {"success": False}
            except Exception as error:
                test_json = {"success": False, "message": f"{error}"}

            result = await session.post(
                url= "",
                json=test_json)
            print(result.status)



asyncio.run(main())