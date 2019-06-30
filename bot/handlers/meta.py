import importlib
#LOGGING
from loguru import logger
from aiogram import Dispatcher

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
