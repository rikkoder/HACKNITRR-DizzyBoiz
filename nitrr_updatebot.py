"""
telegram bot to notify about updates from http://www.nitrr.ac.in/

made by: @rikkoder and @bunnykek
"""

import logging
import os
from importlib import import_module
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

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


# bot token
TOKEN = os.environ.get('TOKEN');


def main() -> None:
    # bot initialization
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # adding command handlers
    for command in commands:
        print(command, commands[command])
        dispatcher.add_handler(CommandHandler(command, commands[command].run))

    print('asdf');
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
