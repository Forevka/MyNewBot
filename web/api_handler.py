from aiohttp import web
from bot import BotObtainer
from datetime import datetime
import settings
from loguru import logger

import string
import random

import collections
import hmac
import hashlib
import json
import jwt

def encode_token(data, token):
    return jwt.encode(data, token, algorithm='HS256')

def decode_token(jwt, token):
    return jwt.decode(jwt, token, algorithms=['HS256'])


def check_string(data, token):
    secret = hashlib.sha256()
    secret.update(token.encode('utf-8'))
    sorted_params = collections.OrderedDict(sorted(data.items()))
    param_hash = data.get('hash', '')
    msg = "\n".join(["{}={}".format(k, v) for k, v in sorted_params.items() if k != 'hash'])

    return param_hash == hmac.new(secret.digest(), msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

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
        headers = {"Access-Control-Allow-Origin": "*",
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'}
        is_from_tg = check_string(data, b['token'])
        logger.debug(is_from_tg)
        if is_from_tg:
            return web.json_response({"status": "ok","token": encode_token(data, b['token']).decode("utf-8") },
                                    headers = headers)
        else:
            return web.json_response({"status": "bad"},
                                    headers = headers)

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
