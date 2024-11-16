from aiogram.fsm.state import StatesGroup, State

class ChooseScheme(StatesGroup):
    ai_ru = State()
    ai_en = State()
    ai_hi = State()
    ai_scrin_ru = State()
    ai_scrin_en = State()
    ai_scrin_hi = State()


class ChooseScheme2(StatesGroup):
    ai2_ru = State()
    ai2_en = State()
    ai2_hi = State()
