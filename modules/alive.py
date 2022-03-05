from telegram import Update
from telegram.ext import CallbackContext

def run(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('nitrr_updatebot is alive')
