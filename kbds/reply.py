from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_kbd(
        *btns: str,
        placeholder: str = None, # type: ignore
        size: tuple[int] = (1,),
):
    kbd = ReplyKeyboardBuilder()
    for index, text in enumerate(btns):
        kbd.add(KeyboardButton(text=text))

    return kbd.adjust(*size).as_markup(resize_keyboard=True)