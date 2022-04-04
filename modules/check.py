from telegram import Update
from telegram.ext import CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode

# adding rootdir to path
import sys, os.path as path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

from lib.scrapper import for_notices

def run(update: Update = None, context: CallbackContext = None, bot = None, chat_id: int = 0, result: list = []) -> None:
    if not chat_id:
        result = for_notices()

    if len(result) == 0:
        update.message.reply_text('No new updates!')
        return;

    msg = f'{len(result)} NEW UPDATES :\n'
    found = 0
    for notice in result:
        found+=1
        title = notice['heading']
        title = escape_markdown(title, version=2)
        link = notice['link']
        link.replace(' ', '%20')
        link = escape_markdown(link, version=2)
        msg += f'\n{found}\. [{title}]({link})\n'

    if chat_id:
        bot.send_message(chat_id=chat_id, text=msg, parse_mode=ParseMode.MARKDOWN_V2)
    else:
        update.message.reply_markdown_v2(msg)
