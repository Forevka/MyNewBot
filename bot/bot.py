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
from aiogram.utils.mixins import ContextInstanceMixin

from datetime import datetime

from .handlers import MetaHandler

class BotController(ContextInstanceMixin):
    def __init__(self, webhook_url, token, full_webhook_path,
                    server = False):
        self.bot = Bot(token=token, parse_mode = "HTML")
        self.dp = Dispatcher(self.bot)
        self.dp.data['start_time'] = datetime.now()
        self.webhook_url = webhook_url
        self.full_webhook_path = full_webhook_path
        Dispatcher.set_current(self.dp)
        Bot.set_current(self.dp.bot)
        BotController.set_current(self)

    def load_handlers(self):
        MetaHandler.register_all()

    def get_bot(self):
        return self.bot

    def get_dispatcher(self):
        return self.dp

    async def configure_app(self, app = None):
        await self.bot.set_webhook(self.full_webhook_path)
        if app is not None:
            configure_app(dispatcher = self.dp, app = app, path = self.webhook_url)
        else:
            return get_new_configured_app(dispatcher=self.dp, path = self.webhook_url)

    def __str__(self):
        return "BotController instance "+str(self.dp.data['start_time'])
