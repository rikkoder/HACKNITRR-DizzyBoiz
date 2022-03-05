from telegram import Update
from telegram.ext import CallbackContext

# adding rootdir to path
import sys, os.path as path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

from lib.scrapper import for_notices

def run(update: Update, context: CallbackContext) -> None:
    result = for_notices()
#     print(result)
    if len(result) == 0:
        update.message.reply_text('No new updates!')
        return;

    msg = f'{len(result)} NEW UPDATES :\n'
    found = 0
    for notice in result:
        found+=1
        title = data[i]['heading']
        print(title)
        title = title.replace('`', '\`')
        title = title.replace('*', '\*')
        title = title.replace('_', '\_')
        title = title.replace('{', '\{')
        title = title.replace('}', '\}')
        title = title.replace('[', '\[')
        title = title.replace(']', '\]')
        title = title.replace('<', '\<')
        title = title.replace('>', '\>')
        title = title.replace('(', '\(')
        title = title.replace(')', '\)')
        title = title.replace('#', '\#')
        title = title.replace('+', '\+')
        title = title.replace('-', '\-')
        title = title.replace('.', '\.')
        title = title.replace('!', '\!')
        title = title.replace('|', '\|')
        print(title)
        link = data[i]['link']
        link = link.split()[0]
        msg += f'\n{found}. [{title}]({link})'

    update.message.reply_markdown_v2(msg)
