from aiohttp import web
from bot import BotController
from datetime import datetime
import settings

class HandlerApi:
    def __init__(self):
        pass

    async def handle_bot_stats(self, request):
        b = BotController.get_current()
        t = b.get_uptime()
        return web.json_response({"when_start":t.strftime(settings.timeformat),
                                    "up_time": str(datetime.now() - t),
                                    "token": b.token})
