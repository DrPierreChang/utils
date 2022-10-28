import asyncio


class MessageError(Exception):
    pass


async def main():
    for i in range(10):
        print(i)

        if i == 11:
            print("Message found!")
            break
    else:
        await asyncio.sleep(10)
        raise MessageError("Message not found!")

asyncio.run(main())