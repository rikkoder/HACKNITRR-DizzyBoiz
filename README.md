A telegram bot that alerts about official updates from http://www.nitrr.ac.in/

HOW TO USE:

the bot is deployed on heroku, you can find the bot at https://t.me/nitrr_updatebot

HOW TO DEPLOY:

remember to add the following environment variables,
herokuAppLink (not required to run on local machine) : get by creating new heroku app
TOKEN : get bot token from BotFather(https://t.me/BotFather)
JSONBLOB, CHATIDBLOB : get from https://jsonblob.com/api

(local machine) you can run the bot on your machine by changing the following line (in nitrr_updatebot.py)

	from
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN, webhook_url=f"{herokuAppLink}{TOKEN}")

	to
	updater.start_polling()
