# -*- coding: utf-8 -*-
import config
import telebot
from datetime import datetime
import time
import random

bot = telebot.TeleBot(config.token)
obz = ['либерахи', 'социал-демократы', 'пропутинцы', 'пидарахи', 'жители прекрассной рассеюшки', 'патриоты', 'политэксперты', 'политологи', 'дети Соловьёва', 'фанаты Киселёва', 'любители боярки']

@bot.message_handler(commands=['start'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	utro = "07:00"
	den = "14:00"
	rabden = "16:40"
	vecher = "20:00"
	noch = "02:00"
	bot.send_message(message.chat.id, "Started in: " + utro + ", " + den + ", " + vecher + ", " + rabden + ", " + noch + ", ")
	while 1:
		a = random.randint(0,len(obz)-1)
		now = datetime.strftime(datetime.now(), "%H:%M")
		if now == utro:
			bot.send_message(message.chat.id, "Доброе утро, " + obz[a])
			time.sleep(60)
			continue
		elif now == den:
			bot.send_message(message.chat.id, "Ну что, " + obz[a] + ", как ваш день проходит?")
			time.sleep(60)
			continue
		elif now == rabden:
			bot.send_message("Эй, "+ obz[a] +", как там пробочки? Чекните https://yandex.ru/maps/51/samara/probki чтоб знать, гордиться страной или нет?")
			time.sleep(60)
			continue
		elif now == vecher:
			bot.send_message(message.chat.id, "Вечер в хату, " + obz[a] + ", сегодня без котлет, хорошего вечера!")
			time.sleep(60)
			continue
		elif now == noch:
			bot.send_message(message.chat.id, "Эй, " + obz[a] + ", спите? А пыня с госдурой новые законы придумывают, пока вы отдыхаете")
			time.sleep(60)
			continue
		else:
			time.sleep(60)
			continue
		

if __name__ == '__main__':
	bot.polling(none_stop=True)