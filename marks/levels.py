from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import sys

sys.path.insert(0, '../')
from fsm import MarksStates, MasteryStates
from misc import dp, mastery, general_markup, general_markup_mastery, nation_markup, bot, marks, mastery


async def generate_markup(nation, mastery=None):
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	range_list = range(5, 11)
	if mastery:
		range_list = range(1, 11)
	for i in range_list:
		markup.insert(InlineKeyboardButton(str(i), callback_data=f"{str(i)} level {nation}"))
	markup.add(InlineKeyboardButton("Вернутся на главную страницу", callback_data="general"))
	return markup


@dp.callback_query_handler(lambda callback_query: True, state=MasteryStates.NATIONS_STATE)
async def callback_handler(query: CallbackQuery):
	nations = {"ussr": "СССР", "germany": "Германия", "usa": "США", "china": "Китай", "france": "Франция",
			   "uk": "Великобритания", "japan": "Япония", "czech": "Чехия", "sweden": "Швеция", "poland": "Польша", "italy": "Италия"}
	if query.data in nations:
		await query.message.edit_text(text=f"Выберите уровень({nations[query.data]}):", reply_markup=await generate_markup(query.data, mastery=True))
	await MasteryStates.next()


@dp.callback_query_handler(lambda callback_query: True, state=MasteryStates.LEVEL_STATE)
async def state_level_mastery(query: CallbackQuery):
	levels = query.data.split()
	if "level" in levels:
		await query.message.edit_text(text=mastery(levels[2], levels[0]), parse_mode='HTML',
									  reply_markup=general_markup())
	elif query.data == 'general':
		await query.message.edit_text(text='Выберите нацию:', reply_markup=nation_markup())
		await MasteryStates.NATIONS_STATE.set()


@dp.callback_query_handler(lambda callback_query: True, state=MarksStates.NATIONS_STATE)
async def some_callback_handler(query: CallbackQuery):
	nations = {"ussr": "СССР", "germany": "Германия", "usa": "США", "china": "Китай", "france": "Франция",
			   "uk": "Великобритания", "japan": "Япония", "czech": "Чехия", "sweden": "Швеция", "poland": "Польша", "italy": "Италия"}
	if query.data in nations:
		await query.message.edit_text(text=f"Выберите уровень({nations[query.data]}):", reply_markup=await generate_markup(query.data))
	await MarksStates.next()


@dp.callback_query_handler(lambda callback_query: True, state=MarksStates.LEVEL_STATE)
async def state_level(query: CallbackQuery):
	levels = query.data.split()
	if "level" in levels:
		await query.message.edit_text(text=marks(levels[2], levels[0]), parse_mode='HTML',
									  reply_markup=general_markup())
	elif query.data == 'general':
		await query.message.edit_text(text='Выберите нацию:', reply_markup=nation_markup())
		await MarksStates.NATIONS_STATE.set()


if __name__ == "__main__":
	print(generate_markup("ussr"))
