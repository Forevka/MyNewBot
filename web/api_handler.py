from aiohttp import web
from bot import BotObtainer
from datetime import datetime
import settings

class HandlerApi:
    def __init__(self):
        pass

    async def get_bot_all(self, request):
        b = BotObtainer.get_current().get_all_bots()
        response = []
        for name, dp in b.items():
            response.append({"name":dp['name'],
                                "start_time": dp['start_time'].strftime(settings.timeformat),
                                "token": dp['token']})
        return web.json_response(response)

    async def get_bot_by_name_token(self, request):
        b = BotObtainer.get_current()
        data = await request.json()
        bot_name = data.get('name')
        bot_token = data.get('token')

        if bot_name:
            bot = b.get_bot_by_name(bot_name)
            if bot:
                return web.json_response({"name": bot['name'],
                                            "start_time": bot['start_time'].strftime(settings.timeformat),
                                            "token":bot['token']})
        if bot_token:
            bot = b.get_bot_by_token(bot_token)
            if bot:
                return web.json_response({"name": bot['name'],
                                            "start_time": bot['start_time'].strftime(settings.timeformat),
                                            "token":bot['token']})

        return web.json_response({"error":"can`t find those bot"})
