"""
telegram bot to notify about updates from http://www.nitrr.ac.in/

made by: @rikkoder and @bunnykek
"""

import threading
import requests
import time
import logging
import os
from importlib import import_module
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from lib.scrapper import for_notices

PORT = int(os.environ.get('PORT', '8443'))

# adding rootdir to path
import sys, os.path as path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

from lib.scrapper import for_notices
from modules.check import run as post_updates

commands = {}
for module in map(lambda x: x[0:-3], filter(lambda x: x[-3:] == '.py' and x[0] != '_', os.listdir('./modules'))):
    try:
        commands[module] = import_module('modules.' + module)
        print(f'imported {module} successfully')
    except ImportError as e:
        print(f'{module} not imported')
        print(e)
    except Exception as e:
        print(e)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# heroku app link
herokuAppLink = os.environ.get('herokuAppLink')

# bot token
TOKEN = os.environ.get('TOKEN');

# chat blob
CHATIDBLOB = os.environ.get('CHATIDBLOB')


# check update
def check_update(bot) -> None:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    response = requests.get(CHATIDBLOB, headers=headers)
    data = response.json()

    chat_ids = []
    if len(data):
        chat_ids = data[0]['chat_ids']


    results = []
    if len(chat_ids):
        results = for_notices()

    if len(results):
        for chat_id in chat_ids:
            post_updates(bot=bot, chat_id=chat_id, result=results)

    # sleep 10 mins
    time.sleep(600)

    check_update(bot)


def main() -> None:
    # bot initialization
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # adding command handlers
    for command in commands:
        print(command, commands[command])
        dispatcher.add_handler(CommandHandler(command, commands[command].run))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN, webhook_url=f"{herokuAppLink}{TOKEN}")

    threading._start_new_thread(check_update, (updater.bot,))
    
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
