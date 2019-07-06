from bot import BotObtainer
from web import HandlerApi
from aiohttp import web
import settings
import logging
import asyncio
import pathlib

import json
import jwt

from aiohttp import web
from loguru import logger


def decode_token(jwt_token, user_token):
    logger.debug(jwt_token)
    logger.debug(user_token)
    decoded = ''
    try:
        decoded = jwt.decode(jwt_token, user_token, algorithms=['HS256'])
    except:
        logger.debug(f"trying to login with falsy token: {jwt_token} and user: {user_token}")
    finally:
        return decoded

def validate_token(jwtoken):
    obtainer = BotObtainer.get_current().get_bot_for_login()
    a = decode_token(jwtoken, obtainer['token'])
    logger.debug(a)
    return a
    #    return True
    #return False

@web.middleware
async def check_auth(request, handler):
    user_token = request.headers.get("auth-token")
    if user_token and validate_token(user_token):
        response = await handler(request)
        return response
    return web.json_response({'status': "unautheticated user"})


# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application()

    bot_pool = BotObtainer(settings.BOT_WEBHOOK_PATH, settings.BOT_WEBHOOK_URL)
    bot_pool.add_bot("bot_1", "697083959:AAEMcQW2EwsXV267zmypRvP6frvREmf9dKo")
    bot_pool.add_bot("bot_2", "631844699:AAEVFt1lUrpQGaDiDZ7NpbunNRWezY8nXn0")
    bot_pool.set_bot_for_login("bot_1")
    bot_pool.configure_app(app)
    bot_pool.load_handlers()
    #for name, cur_dp in bot_pool.get_all_bots().items():
    #    loop.run_until_complete(bot_pool.set_webhook(name))
    handler_api = HandlerApi()
    app.router.add_route('post', '/approve_user', handler_api.approve_user)
    app.router.add_route('get', "/", handler_api.show_site)
    app.router.add_static('/static', "dist/static", show_index=True)

    admin_app = web.Application(middlewares=[check_auth])
    admin_app.router.add_route('post', '/ping', handler_api.ping)
    admin_app.router.add_route('post', '/get_all_bots', handler_api.get_bot_all)
    admin_app.router.add_route('post', '/get_bot', handler_api.get_bot_by_name_token)
    app.add_subapp('/admin/', admin_app)

    for i in app.router.routes():
        print(i)
    web.run_app(app, host=settings.WEBAPP_HOST, port=settings.WEBAPP_PORT)
