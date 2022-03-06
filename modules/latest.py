from telegram import Update
from telegram.ext import CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode

# adding rootdir to path
import sys, os.path as path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

from lib.scrapper import get_json

def run(update: Update, context: CallbackContext) -> None:
    data = get_json()

    if len(data) == 0:
        update.message.reply_text('No Notices To Show!')
        return;

    count = 5
    if len(context.args) != 0 and context.args[0].isnumeric():
        count = int(context.args[0])

    found = 0
    msg = ''
    for i in range(count):
        if i>=len(data):
            break
        found+=1
        title = data[i]['heading']
        title = escape_markdown(title, version=2)
        link = data[i]['link']
        link = link.replace(' ', '%20')
        link = escape_markdown(link, version=2)
        msg += f'\n{i+1}\. [{title}]({link})\n'

    msg = f'{found} LATEST UPDATES :\n' + msg

    update.message.reply_markdown_v2(msg)
