import base64
import asyncio


login = 'admin'
password = 'admin'

async def get_base64_credentials(login, password):
    credentials = f'{login}:{password}'
    base64_credentials = base64.b64encode(credentials.encode())
    credentials=f'Basic {base64_credentials.decode()}'

    print(credentials)

asyncio.run(get_base64_credentials(login, password))
