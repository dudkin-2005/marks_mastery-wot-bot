from aiogram import executor
from fsm import MarksStates, MasteryStates
from misc import dp, bot, nation_markup
from marks import at_svg, levels
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
	item1 = KeyboardButton('Отметки')
	item2 = KeyboardButton('Степени')
	item3 = KeyboardButton('О боте')
	markup.add(item1, item2, item3)
	await message.reply("Выберите", reply_markup=markup)

@dp.message_handler(state='*')
async def text_in_start(message: types.Message):
	if message.text == 'Отметки':
		await MarksStates.NATIONS_STATE.set()
		await message.reply(text="Выберите нацию:", reply_markup=nation_markup())
	elif message.text == 'Степени':
		await MasteryStates.NATIONS_STATE.set()
		await message.reply(text="Выберите нацию:", reply_markup=nation_markup())
	elif message.text == 'О боте':
		await message.reply(text='Все данные взяты из https://lebwa.tv/\n\nБота сделал @ivolfram')

async def shutdown(dispatcher: dp):
	await dispatcher.storage.close()
	await dispatcher.storage.wait_closed()

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)