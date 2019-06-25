from aiohttp import web

class HandlerSite:
    def __init__(self):
        pass

    async def handle_intro(self, request):
        return web.Response(text="Hello, world")
