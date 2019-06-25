from bot import MyBot
from web_site import HandlerSite
from aiohttp import web
import settings
import logging

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8888

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = web.Application()
    b = MyBot(settings.WEBHOOK_URL_PATH, settings.API_TOKEN)
    b.load_handlers()
    b.configure_app(app)
    handler = HandlerSite()
    app.router.add_post('/intro', handler.handle_intro)
    for i in app.router.routes():
        print(i)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    #executor.start_polling(dp, skip_updates=True)
