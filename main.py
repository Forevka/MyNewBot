from bot import BotController
from web_site import HandlerSite, HandlerApi
from aiohttp import web
import settings
import logging
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application()
    b = BotController(settings.BOT_WEBHOOK_PATH, settings.API_TOKEN, settings.BOT_WEBHOOK_URL)
    b.load_handlers()
    loop.run_until_complete(b.configure_app(app))
    handler_site = HandlerSite(app)
    handler_api = HandlerApi()
    app.router.add_route('get',  '/intro',    handler_site.handle_intro)
    app.router.add_route('post', '/bot_time', handler_api.handle_bot_uptime)
    for i in app.router.routes():
        print(i)
    web.run_app(app, host=settings.WEBAPP_HOST, port=settings.WEBAPP_PORT)
    #executor.start_polling(dp, skip_updates=True)
