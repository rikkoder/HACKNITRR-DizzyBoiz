import os
import requests
from telegram import Update
from telegram.ext import CallbackContext

CHATIDBLOB = os.environ.get('CHATIDBLOB')

def run(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id

    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }


        response = requests.get(CHATIDBLOB, headers=headers)
        data = response.json()

        chat_ids = []
        if len(data):
            chat_ids = data[0]['chat_ids']

        if not chat_id in chat_ids:
            update.message.reply_text('already disabled!')

        else:
            chat_ids = list(filter(lambda x: x!= chat_id, chat_ids))
            data = [{"chat_ids": chat_ids}]

            response = requests.put(CHATIDBLOB, headers=headers, json=data)
            update.message.reply_text('auto notification disabled!')

    except Exception as e:
        print(e)
        update.message.reply_text('Something Went Wrong!\nUnable to disable auto notification :(')
