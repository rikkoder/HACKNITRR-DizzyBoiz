from telegram import Update
from telegram.ext import CallbackContext

def run(update: Update, context: CallbackContext) -> None:
    update.message.reply_markdown_v2(
        f'This bot gives notification about official updates from [NIT Raipur official site](http://www.nitrr.ac.in/)',
    )
