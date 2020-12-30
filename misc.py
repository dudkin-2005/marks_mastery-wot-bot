import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from markswot import MarksWot

bot = Bot(token="")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

def marks(nation, level):
	d1 = list(MarksWot(nation=nation, level=level).get_marks().items())
	text = ''
	for i in d1:
		name = i[0]
		onemark = i[1][0]
		twomark = i[1][1]
		threemark = i[1][2]
		hundredmark = i[1][3]			
		text += '• ' + f'<b>{name}</b>' + f' 65% - {onemark} урона, 85% - {twomark} урона, 95% - {threemark} урона, 100% - {hundredmark} урона' + '\n\n'
	return text

def mastery(nation, level):
	d1 = list(MarksWot(nation=nation,level=level).get_mastery().items())
	text = ''
	for i in d1:
		name = i[0]
		onemark = i[1][0]
		twomark = i[1][1]
		threemark = i[1][2]
		hundredmark = i[1][3]			
		text += '• ' + f'<b>{name}</b>' + f' 3 степень - {onemark} опыта, 2 степень - {twomark} опыта, 1 степень - {threemark} опыта, Мастер - {hundredmark} опыта' + '\n\n'
	return text

def general_markup_mastery():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(InlineKeyboardButton("Вернутся на главную страницу", callback_data="general_m"))
	return markup

def general_markup():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(InlineKeyboardButton("Вернутся на главную страницу", callback_data="general"))
	return markup

def nation_markup():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(InlineKeyboardButton("🇷🇺СССР", callback_data="ussr"), 
		InlineKeyboardButton("🇩🇪Германия", callback_data="germany"), 
		InlineKeyboardButton("🇺🇸США", callback_data="usa"),
		InlineKeyboardButton("🇨🇳Китай", callback_data="china"),
		InlineKeyboardButton("🇫🇷Франция", callback_data="france"),
		InlineKeyboardButton("🇬🇧Великобритания", callback_data="uk"),
		InlineKeyboardButton("🇯🇵Япония", callback_data="japan"),
		InlineKeyboardButton("🇨🇿Чехия", callback_data="czech"),
		InlineKeyboardButton("🇸🇪Швеция", callback_data="sweden"),
		InlineKeyboardButton("🇵🇱Польша", callback_data="poland"),
		InlineKeyboardButton("🇮🇹Италия", callback_data="italy"),)
	return markup

if __name__ == "__main__":
	print(mastery("ussr", "6"))
