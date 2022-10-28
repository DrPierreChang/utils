import asyncio
import aiohttp

def exc_handler(loop, context):
    if context["message"] == "Unclosed connection":
        return
    loop.default_exception_handler(context)


async def main(i=10):
    for j in range(i):
        async with aiohttp.ClientSession() as session:
            # asyncio.get_running_loop().set_exception_handler(exc_handler)
            resp = await session.get('')
            await resp.text()
            # resp.close()
            print(j, resp.closed)
        # print(session.closed)
        # print("resp closed: ", resp.closed)
            
    print('done {}'.format(i))


if __name__ == "__main__":
    asyncio.run(main())
