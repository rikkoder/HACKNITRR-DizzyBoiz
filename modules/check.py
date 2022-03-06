from telegram import Update
from telegram.ext import CallbackContext
from telegram.utils.helpers import escape_markdown

# adding rootdir to path
import sys, os.path as path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

from lib.scrapper import for_notices

def run(update: Update, context: CallbackContext) -> None:
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

    update.message.reply_markdown_v2(msg)
