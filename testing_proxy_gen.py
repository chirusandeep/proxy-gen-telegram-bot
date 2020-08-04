from telegram.ext import Updater, CommandHandler
from datetime import datetime
import requests
import pytz
import os


PORT = int(os.environ.get('PORT', 5000))
TOKEN = 'your_telegram_token_here'


def checker(proxytext):
    proxylist = proxytext.split("\r\n")
    proxylist.remove('')
    working_proxy = []
    for proxy in proxylist:
        proxy = proxy.split(':')
        data = {"ip_addr": proxy[0], "port": proxy[1]}

        response = requests.post('https://onlinechecker.proxyscrape.com/index.php', data=data)
        x = response.json()

        ip = x["ip"]
        port = x["port"]
        type = x["type"]
        country = x["country"]
        working = x["working"]
        if working:
            working_proxy += [ip + ":" + port + " " + type + " " + country + "\n"]
    return working_proxy


def http(update, context):
    http = requests.get(
        'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=50&country=all&ssl=yes&anonymity=all')
    update.message.reply_text("Please wait processing...")
    if http.text != '' or None:
        workinghttp = checker(http.text)
        if workinghttp != []:
            update.message.reply_text("Proxy Type Country\n==================\n{}".format(''.join(workinghttp)))
        else:
            update.message.reply_text("Not available right now.\nCheck back in 10min!")
    else:
        update.message.reply_text("Not available right now.\nCheck back in 10min!")
    print(update.message.chat_id, update.message.from_user.username, update.message.from_user.first_name,
          update.message.from_user.last_name, "http", datetime.now(pytz.timezone('Asia/Kolkata')))


def socks4(update, context):
    socks4 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=50&country=all')
    update.message.reply_text("Please wait processing...")
    if socks4.text != '' or None:
        workingsocks4 = checker(socks4.text)
        if workingsocks4 != []:
            update.message.reply_text("Proxy Type Country\n==================\n{}".format(''.join(workingsocks4)))
        else:
            update.message.reply_text("Not available right now.\nCheck back in 10min!")
    else:
        update.message.reply_text("Not available right now.\nCheck back in 10min!")
    print(update.message.chat_id, update.message.from_user.username, update.message.from_user.first_name,
          update.message.from_user.last_name, "socks4", datetime.now(pytz.timezone('Asia/Kolkata')))


def socks5(update, context):
    socks5 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=50&country=all')
    update.message.reply_text("Please wait processing...")
    if socks5.text != '' or None:
        workingsocks5 = checker(socks5.text)
        if workingsocks5 != []:
            update.message.reply_text("Proxy Type Country\n==================\n{}".format(''.join(workingsocks5)))
        else:
            update.message.reply_text("Not available right now.\nCheck back in 10min!")
    else:
        update.message.reply_text("Not available right now.\nCheck back in Later!")
    print(update.message.chat_id, update.message.from_user.username, update.message.from_user.first_name,
          update.message.from_user.last_name, "socks5", datetime.now(pytz.timezone('Asia/Kolkata')))


def Whatisproxy(update, context):
    update.message.reply_photo('https://cdn.whatismyipaddress.com/images-v4/how-proxies-work.png')
    print(update.message.chat_id, update.message.from_user.username, update.message.from_user.first_name,
          update.message.from_user.last_name, "start", datetime.now(pytz.timezone('Asia/Kolkata')))


def start(update, context):
    items = '''

    info: /what_is_proxy

    List of proxy items
    ===================

    http proxies   = /http
    socks4 proxies = /socks4
    socks5 proxies = /socks5

    Press /start to get this list.
    
    '''
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
    update.message.reply_text(items)
    print(update.message.chat_id, update.message.from_user.username, update.message.from_user.first_name,
          update.message.from_user.last_name, "start", datetime.now(pytz.timezone('Asia/Kolkata')))


updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('what_is_proxy', Whatisproxy))
updater.dispatcher.add_handler(CommandHandler('http', http))
updater.dispatcher.add_handler(CommandHandler('socks4', socks4))
updater.dispatcher.add_handler(CommandHandler('socks5', socks5))

updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
updater.bot.setWebhook('https://proxyreq.herokuapp.com/' + TOKEN)
updater.idle()
