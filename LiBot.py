# -*- coding: utf-8 -*-
import config
import telebot
from datetime import datetime
import time
import random

bot = telebot.TeleBot(config.token)
obz = ['либерахи', 'социал-демократы', 'пропутинцы', 'пидарахи', 'жители прекрассной рассеюшки', 'патриоты', 'политэксперты', 'политологи', 'дети Соловьёва', 'фанаты Киселёва', 'любители боярки']
a = random.randint(0,len(obz)-1)

@bot.message_handler(commands=['start'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	destiny = "14:27"
	bot.send_message(message.chat.id, "Заебок, теперь, когда будет: " + destiny + " я напишу хуйню в чат, больше не хуярьте мне команды пока")
	while 1:
		now = datetime.strftime(datetime.now(), "%H:%M")
		if now == destiny:
			bot.send_message(message.chat.id, "Доброе утро, "+obz[a])
			time.sleep(60)
			continue
		else:
			bot.send_message(message.chat.id, "Пока не время")
			time.sleep(60)
			continue
		

if __name__ == '__main__':
	bot.polling(none_stop=True)