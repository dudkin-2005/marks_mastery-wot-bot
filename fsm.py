from aiogram.dispatcher.filters.state import State, StatesGroup


class MarksStates(StatesGroup):
    NATIONS_STATE = State()
    LEVEL_STATE = State()


class MasteryStates(StatesGroup):
    NATIONS_STATE = State()
    LEVEL_STATE = State()
