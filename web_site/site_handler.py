from aiohttp import web
import aiohttp_jinja2
import jinja2
from pathlib import Path

class HandlerSite:
    def __init__(self, app):
        here = 'web_site/templates'
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(here)))

    #@aiohttp_jinja2.template('index.html')
    async def handle_intro(self, request):
        return web.Response(
        text=open('web_site/templates/index.html', "r").read(),
        content_type='text/html')
        #return {'name': 'Get Bot UpTime'}

    @aiohttp_jinja2.template('js/index.js')
    async def handle_js_intro(self, request):
        return {}
