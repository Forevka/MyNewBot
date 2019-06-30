import logging

from aiogram import Bot, Dispatcher, executor, types
import asyncio
import ssl
import sys
from aiohttp import web

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app, configure_app,\
                                        WebhookRequestHandler, BOT_DISPATCHER_KEY,\
                                        DEFAULT_WEB_PATH, DEFAULT_ROUTE_NAME
from aiogram.types import ChatType, ParseMode, ContentTypes
from aiogram.utils.markdown import hbold, bold, text, link
from aiogram.utils.mixins import ContextInstanceMixin

from datetime import datetime

from .handlers import MetaHandler

def my_configure_app(dispatcher, app: web.Application, path=DEFAULT_WEB_PATH, route_name=DEFAULT_ROUTE_NAME):
    """
    You can prepare web.Application for working with webhook handler.
    :param dispatcher: Dispatcher instance
    :param app: :class:`aiohttp.web.Application`
    :param path: Path to your webhook.
    :param route_name: Name of webhook handler route
    :return:
    """

    app.router.add_route('*', path, MyWebhookRequestHandler, name=route_name)
    app[path] = dispatcher

class MyWebhookRequestHandler(WebhookRequestHandler):
    def get_dispatcher(self):
        dp = self.request.app[self.request.path]
        try:
            from aiogram import Bot, Dispatcher
            Dispatcher.set_current(dp)
            Bot.set_current(dp.bot)
        except RuntimeError:
            pass
        return dp

class BotPool:
    bot_alias = {}

    @staticmethod
    def add_bot(name, bot_token, ignore_exist = True):
        bot = Bot(token=bot_token, parse_mode = "HTML")
        dp = Dispatcher(bot)
        dp.data['token'] = bot_token
        dp.data['name'] = name
        dp.data['start_time'] = datetime.now()
        if BotPool.bot_alias.get(name) is None:
            BotPool.bot_alias[name] = dp
        else:
            if ignore_exist:
                BotPool.bot_alias[name] = dp
            else:
                return None

        return dp

    @staticmethod
    def get_all_bots():
        return BotPool.bot_alias

    @staticmethod
    def get_bot_by_name(name):
        return BotPool.bot_alias.get(name)

    @staticmethod
    def get_bot_by_token(token):
        for dp in BotPool.bot_alias.values():
            if dp.data['token'] == token:
                return dp

        return None

    @staticmethod
    def configure_app(webhook_path, app = None):
        if app is None:
            app = web.Application()

        for name, cur_dp in BotPool.bot_alias.items():
            this_bot = cur_dp.bot
            my_configure_app(dispatcher = cur_dp, app = app,
                            path = webhook_path+name,
                            route_name = "webhook_"+name, )

        return app

class BotObtainer(ContextInstanceMixin):
    def __init__(self, webhook_url, full_webhook_path,
                    server = False):
        self.webhook_url = webhook_url
        self.full_webhook_path = full_webhook_path

        BotObtainer.set_current(self)

    def add_bot(self, name, token, ignore_exist = True):
        return BotPool.add_bot(name, token, ignore_exist = True)

    def load_handlers(self):
        for name, cur_dp in self.get_all_bots().items():
            MetaHandler.register_all(cur_dp)

    def get_all_bots(self):
        return BotPool.get_all_bots()

    def get_bot_by_name(self, name):
        return BotPool.get_bot_by_name(name)

    def get_bot_by_token(self, token):
        return BotPool.get_bot_by_token(token)

    def configure_app(self, app = None):
        return BotPool.configure_app(self.webhook_url, app = app)

    async def set_webhook(self, bot_name):
        cur_dp = BotPool.get_bot_by_name(bot_name)
        return await cur_dp.bot.set_webhook(self.full_webhook_path + cur_dp.data['name'])

    def __str__(self):
        return "BotObtainer instance"
