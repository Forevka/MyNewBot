import importlib
#LOGGING
from loguru import logger
from aiogram import Dispatcher, types

class MetaHandler(object):
    @staticmethod
    def register_all(dp = None):
        if dp is None:
            dp = Dispatcher.get_current()

        handlers_module = importlib.import_module('.handlers_bot', package='bot.handlers')
        for handler in handlers_module.__all__:
            logger.debug(f"loading {handler}")
            handler = getattr(handlers_module, handler)
            handler_ = handler(dp)
            handler_.register()

    def register(self):
        logger.error(f"Need to Implement register method in {self.__class__.__name__}")
        #raise BaseException(f"Need to Implement register method in {self.__class__.__name__}")

class LoginHandler:
    def __init__(self, dp = None):
        self.dp = dp

    def register(self, dp):
        self.dp = dp
        self.dp.register_message_handler(self.login_user, commands = 'start')
        #self.dp.register_message_handler(self.get_login_button, commands = 'login')

    async def get_login_button(self, message: types.Message):
        markup = types.InlineKeyboardMarkup()
        a = types.LoginUrl("forevka.serveo.net%2F%23%2Flogin")
        b = types.InlineKeyboardButton('Login to site', login_url = a)
        logger.debug(a)
        logger.debug(b)
        markup.add(b)
        await message.answer(f'Код подтверждение для сайта {self.dp.data["approve_code"]}', reply_markup = markup)
