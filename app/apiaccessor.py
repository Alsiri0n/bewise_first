import aiohttp
from aiohttp import TCPConnector
from aiohttp.client import ClientSession
from .models import APIResponse


class APIAccessor:
    def __init__(self):
        self.session: ClientSession | None = None

    async def get_data(self, url: str) -> list[APIResponse | None]:
        self.session = ClientSession(connector=TCPConnector(verify_ssl=False))
        q = []
        try:
            async with self.session.get(url) as resp:
                data = await resp.json()
            for d in data:
                q.append(APIResponse.parse_obj(d))
        except Exception as e:
            print("Exception", e)
        finally:
            await self.session.close()
            return q
