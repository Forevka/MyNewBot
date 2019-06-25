from bot import BotController
from web_site import HandlerSite, HandlerApi
from aiohttp import web
import settings
import logging

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8888

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = web.Application()
    b = BotController(settings.WEBHOOK_URL_PATH, settings.API_TOKEN)
    b.load_handlers()
    b.configure_app(app)
    handler_site = HandlerSite()
    handler_api = HandlerApi()
    app.router.add_post('/intro', handler_site.handle_intro)
    app.router.add_post('/bot_time', handler_api.handle_bot_uptime)
    for i in app.router.routes():
        print(i)
    print(BotController.get_current())
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    #executor.start_polling(dp, skip_updates=True)
