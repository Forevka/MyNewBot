from aiohttp import web
from bot import BotController

class HandlerApi:
    def __init__(self):
        pass

    async def handle_bot_uptime(self, request):
        return web.Response(text="Bot Lives Time: " + str(BotController.get_current()))
