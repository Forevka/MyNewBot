##############################################
# FOR START TUNNEL                           #
# ssh -R forevka:443:localhost:443 serveo.net#
##############################################

API_TOKEN = '697083959:AAEMcQW2EwsXV267zmypRvP6frvREmf9dKo'

SERVER_HOST = 'forevka.serveo.net'  # Domain name or IP addres which your bot is located.
SERVER_PORT = 443  # Telegram Bot API allows only for usage next ports: 443, 80, 88 or 8443


# This options needed if you use self-signed SSL certificate
# Instructions: https://core.telegram.org/bots/self-signed
WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

BOT_WEBHOOK_PATH = '/webhook'  # Part of URL
BOT_WEBHOOK_URL = f"https://{SERVER_HOST}:{SERVER_PORT}{BOT_WEBHOOK_PATH}"

# Web app settings:
#   Use LAN address to listen webhooks
#   User any available port in range from 1024 to 49151 if you're using proxy, or WEBHOOK_PORT if you're using direct webhook handling
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 443
