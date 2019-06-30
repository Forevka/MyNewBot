from aiogram import Bot, Dispatcher, executor, types
#LOGGING
from loguru import logger

from ..meta import MetaHandler

class MainHandler(MetaHandler):
    def __init__(self, dp):
        self.dp = dp

    def register(self):
        self.dp.register_message_handler(self.echo)

    async def echo(self, message: types.Message):
        await message.answer(message.text)
