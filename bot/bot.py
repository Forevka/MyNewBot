import logging

from aiogram import Bot, Dispatcher, executor, types
import asyncio
import ssl
import sys

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app, configure_app
from aiogram.types import ChatType, ParseMode, ContentTypes
from aiogram.utils.markdown import hbold, bold, text, link

from .handlers import MetaHandler

class MyBot:
    def __init__(self, webhook_url, token,
                    server = False):
        self.bot = Bot(token=token, parse_mode = "HTML")
        self.dp = Dispatcher(self.bot)
        self.webhook_url = webhook_url
        Dispatcher.set_current(self.dp)
        Bot.set_current(self.dp.bot)

    def load_handlers(self):
        MetaHandler.register_all()

    def get_bot(self):
        return self.bot

    def get_dispatcher(self):
        return self.dp

    def configure_app(self, app = None):
        if app is not None:
            configure_app(dispatcher = self.dp, app = app, path = self.webhook_url)
        else:
            return get_new_configured_app(dispatcher=self.dp, path = self.webhook_url)
