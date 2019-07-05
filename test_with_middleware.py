from aiohttp import web

def validate_token(token, key):
    if token == "qwert":
        return True
    return False

@web.middleware
async def check_auth(request, handler):
    user_token = request.headers.get("auth-token")
    if user_token and validate_token(user_token, "bot_token"):
        response = await handler(request)
        return response
    return web.json_response({'error': "unautheticated user"})


async def hello(request):
    return web.json_response({"payload":"ok"})

app = web.Application(middlewares=[check_auth])
app.add_routes([web.post('/test_token', hello)])

web.run_app(app)
