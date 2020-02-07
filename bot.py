from telegram import Bot, Update

from telegram.ext import MessageHandler, Filters, Updater


TG_TOKEN = '1064447858:AAE6oYtA3jfe0w0rzXPTmEWGHlRdIwtc-Mk'

def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'Гость'

	text = update.effective_message.text
	reply_text = f'Привет, {name}!\n\n{text}'

	bot.send_message(
		chat_id=update.effective_message.chat_id,
		text=reply_text,
		)

def main():
	print('Start')
	bot = Bot(token=TG_TOKEN,)
	updater = Updater(bot=bot)

	handler = MessageHandler(Filters.all, message_handler)
	updater.dispatcher.add_handler(handler)

	updater.start_polling()
	updater.idle()
	print('Finish')



if __name__ == '__main__':
	main()