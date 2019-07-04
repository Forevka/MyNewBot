from aiohttp import web
from bot import BotObtainer
from datetime import datetime
import settings
from loguru import logger

import string
import random
def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

class HandlerApi:
    def __init__(self):
        pass

    async def user_logged(self, request):
        data = request.rel_url.query
        logger.debug(data)
        return web.json_response({})

    async def show_site(self, request):
        return web.Response(text=open("dist/index.html").read(), content_type='text/html')

    async def approve_user(self, request):
        b = BotObtainer.get_current().get_bot_for_login()
        logger.debug(request)
        data = await request.json()
        logger.debug(data)
        if b.data['approve_code'] == data['approve_code']:
            return web.json_response({"status": "ok","token": f"here-will-be-token"},
                                    headers = {"Access-Control-Allow-Origin": "*"})
        else:
            return web.json_response({"status": "bad"},
                                    headers = {"Access-Control-Allow-Origin": "*"})


    async def login_user(self, request):
        b = BotObtainer.get_current().get_bot_for_login()
        b['login_code'] = randomString(8)
        b['login_time'] = datetime.now()
        bot_username = await b.bot.get_me()
        response = {"url": f"http://t.me/{bot_username.username}?start={b['login_code']}"}
        return web.json_response(response,
                                headers = {"Access-Control-Allow-Origin": "*"})

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
