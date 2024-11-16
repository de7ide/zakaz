from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_kbd(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (1,)
):
    kbrd = InlineKeyboardBuilder()
    for text, value in btns.items():
        if '://' in value:
            kbrd.add(InlineKeyboardButton(text=text, url=value))
        else:
            kbrd.add(InlineKeyboardButton(text=text, callback_data=value))

    return kbrd.adjust(*sizes).as_markup()
