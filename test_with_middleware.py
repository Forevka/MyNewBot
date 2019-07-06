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


async def with_token(request):
    return web.json_response({"payload":"with_token"})

async def without_token(request):
    return web.json_response({"payload":"without_token"})

root_app = web.Application()


admin_app = web.Application(middlewares=[check_auth])
admin_app.add_routes([web.post('/test_token', with_token)])

root_app.add_routes([web.post('/test', without_token)])

root_app.add_subapp('/admin/', admin_app)
for i in root_app.router.routes():
    print(i)
web.run_app(root_app, port = 7890)
