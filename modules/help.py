from telegram import Update
from telegram.ext import CallbackContext

# adding rootdir to path
import sys, os.path as path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

from docs.cmd_info import HELP_MESSAGES

def run(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0 or not context.args[0] in HELP_MESSAGES:
        update.message.reply_text(HELP_MESSAGES['general'])

    else:
        update.message.reply_text(HELP_MESSAGES[context.args[0]])
