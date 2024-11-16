import asyncio
import random

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove, User
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state


from lexicon.lexicon import LEXICON_EN, LEXICON_RU, LEXICON_HINDI
from kbds.reply import get_kbd
from kbds.inline import get_inline_kbd
from utils.state import ChooseScheme, ChooseScheme2


user_languages = {}

user_router = Router()

photoEn = FSInputFile('lexicon/eng.jpg')
photoRu = FSInputFile('lexicon/russ.jpg')
photoHI = FSInputFile('lexicon/hindi.jpg')


@user_router.message(CommandStart())
async def start_comm(message: Message):
    await message.answer(text="Language 🌏", reply_markup=get_inline_kbd(
        btns={
            "English 🇺🇸": 'en_butt',
            "Русский 🇷🇺": 'ru_butt',
            "हिन्दी 🇮🇳": 'hi_butt',
        }))


###start en menu
@user_router.callback_query(F.data == 'en_butt')
async def press_en_but(callback: CallbackQuery):
    await callback.message.delete() # type: ignore
    await callback.message.answer_photo(photo=photoEn, caption=LEXICON_EN['caption'], reply_markup=get_kbd("📖 Schemes", "📣 My chanal", "💬 Reviews", size=(2,1))) # type: ignore
    await callback.answer()


###start ru menu
@user_router.callback_query(F.data == 'ru_butt')
async def press_ru_but(callback: CallbackQuery):
    await callback.message.delete() # type: ignore
    await callback.message.answer_photo(photo=photoRu, caption=LEXICON_RU['caption'], reply_markup=get_kbd("📖 Схемы", "📣 Мой канал", "💬 Отзывы", size=(2,))) # type: ignore
    await callback.answer()

###start hi menu
@user_router.callback_query(F.data == 'hi_butt')
async def press_hi_but(callback: CallbackQuery):
    await callback.message.delete() # type: ignore
    await callback.message.answer_photo(photo=photoHI, caption=LEXICON_HINDI['caption'], reply_markup=get_kbd("📖 योजनाओं", "📣 मेरा चैनल", "💬 समीक्षा ", size=(2,1))) # type: ignore
    await callback.answer()

###
@user_router.message(F.text == '📖 Схемы')
async def schemes_ru(message: Message):
    await message.answer(text='Выберите доступные схемы:', reply_markup=get_kbd("AI Анализ🤖", "🎲 Накрутка Удачи", "❌ Крестики Нолики", "🔙 Назад", size=(1,)))


@user_router.message(F.text == '📖 Schemes')
async def schemes_en(message: Message):
    await message.answer(text='Select available schemes:', reply_markup=get_kbd("AI Analysis🤖", "🎲 Cheat Luck", "❌ Tic Tac Toe", "🔙 Back", size=(1,)))


@user_router.message(F.text == '📖 योजनाओं')
async def schemes_hi(message: Message):
    await message.answer(text='उपलब्ध योजनाओं का चयन करें:', reply_markup=get_kbd("एआई विश्लेषण🤖", "🎲 धोखा किस्मत", "❌ टिक टीएसी को पैर की अंगुली", "🔙 पीछे", size=(1,)))

###AI ANalisys
@user_router.message(F.text == 'AI Анализ🤖')
async def ai_ru(message: Message):
    await message.answer(text='Выберите доступные действия:', reply_markup=get_kbd("📄 Схема", "🤖AI Анализ", "🔙Назад", size=(1,)))


@user_router.message(F.text == 'AI Analysis🤖')
async def ai_en(message: Message):
    await message.answer(text='Select available actions:', reply_markup=get_kbd("📄 Scheme", "🤖AI Analysis", "🔙Back", size=(1,)))


@user_router.message(F.text == 'एआई विश्लेषण🤖')
async def ai_hi(message: Message):
    await message.answer(text='उपलब्ध क्रियाएँ चुनें:', reply_markup=get_kbd("📄 योजना", "🤖एआई विश्लेषण", "🔙पीछे ", size=(1,)))


@user_router.message(F.text == "📄 Схема")
async def scheme_ru(message: Message):
    await message.answer(text='https://telegra.ph/AI-Analiz-11-08')


@user_router.message(F.text == "📄 Scheme")
async def scheme_en(message: Message):
    await message.answer(text='https://telegra.ph/AI-Analiz-11-08')


@user_router.message(F.text == "📄 योजना")
async def scheme_hi(message: Message):
    await message.answer(text='https://telegra.ph/%E0%A4%8F%E0%A4%86%E0%A4%88-%E0%A4%B5%E0%A4%B6%E0%A4%B2%E0%A4%B7%E0%A4%A3-11-08')


@user_router.message(StateFilter(None), F.text == '🤖AI Анализ')
async def ai_st_ru(message: Message, state: FSMContext):
    await message.answer(text='Отправьте ID',reply_markup=ReplyKeyboardRemove())
    await state.set_state(ChooseScheme.ai_ru)


@user_router.message(StateFilter(None), F.text == '🤖AI Analysis')
async def ai_st_en(message: Message, state: FSMContext):
    await message.answer(text='Send ID', reply_markup=ReplyKeyboardRemove())
    await state.set_state(ChooseScheme.ai_en)


@user_router.message(StateFilter(None), F.text == '🤖एआई विश्लेषण')
async def ai_st_hi(message: Message, state: FSMContext):
    await message.answer(text='ऑप्शंस आईडी', reply_markup=ReplyKeyboardRemove())
    await state.set_state(ChooseScheme.ai_hi)


@user_router.message(ChooseScheme.ai_ru, F.text)
async def answ_ai_ru(message: Message, state: FSMContext):
    await state.update_data(ai=message.text)
    await message.answer("Успешно ✅", reply_markup=get_kbd("📄 Схема", "🤖AI Анализ", "🔙Назад", size=(1,)))
    await state.set_state(ChooseScheme.ai_scrin_ru)


@user_router.message(ChooseScheme.ai_en, F.text)
async def answ_ai_en(message: Message, state: FSMContext):
    await state.update_data(ai=message.text)
    await message.answer("Successfully  ✅", reply_markup=get_kbd("📄 Scheme", "🤖AI Analysis", "🔙Back", size=(1,)))
    await state.set_state(ChooseScheme.ai_scrin_en)


@user_router.message(ChooseScheme.ai_hi, F.text)
async def answ_ai_hi(message: Message, state: FSMContext):
    await state.update_data(ai=message.text)
    await message.answer("सफलतापूर्वक ✅", reply_markup=get_kbd("📄 योजना", "🤖एआई विश्लेषण", "🔙पीछे ", size=(1,)))
    await state.set_state(ChooseScheme.ai_scrin_hi)


@user_router.message(ChooseScheme.ai_scrin_ru, F.photo)
async def ai_scrin_ru(message: Message, state: FSMContext, bot: Bot):
    await message.answer('Анализ...')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action='typing') # type: ignore
    await asyncio.sleep(2)
    rn = random.randint(00, 99)
    rn2 = random.randint(70, 99)
    await message.answer(text=f"Забрать на 1.{rn}\n📊 Шанс {rn2}%")
    await state.clear()


@user_router.message(ChooseScheme.ai_scrin_en, F.photo)
async def ai_scrin_en(message: Message, state: FSMContext, bot: Bot):
    await message.answer('Analysis...')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action='typing') # type: ignore
    await asyncio.sleep(2)
    rn = random.randint(00, 99)
    rn2 = random.randint(70, 99)
    await message.answer(text=f"Pick up at 1.{rn}\n📊 Chance {rn2}%")
    await state.clear()


@user_router.message(ChooseScheme.ai_scrin_hi, F.photo)
async def ai_scrin_hi(message: Message, state: FSMContext, bot: Bot):
    await message.answer('विश्लेषण...')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action='typing') # type: ignore
    await asyncio.sleep(2)
    rn = random.randint(00, 99)
    rn2 = random.randint(70, 99)
    await message.answer(text=f"पर उठाओ 1.{rn}\n📊 मौका {rn2}%")
    await state.clear()


#back button 1
@user_router.message(F.text == '🔙 Назад')
async def back1_ru(message: Message):
    await message.answer('Вы вернудись в предыдущее меню...', reply_markup=get_kbd("📖 Схемы", "📣 Мой канал", "💬 Отзывы", size=(2,)))


@user_router.message(F.text == '🔙 Back')
async def back1e_en(message: Message):
    await message.answer('You are back to the previous menu...', reply_markup=get_kbd("📖 Schemes", "📣 My chanal", "💬 Reviews", size=(2,)))


@user_router.message(F.text == '🔙 पीछे')
async def back1e_hi(message: Message):
    await message.answer('आप पिछले मेनू पर वापस आ गए हैं...', reply_markup=get_kbd("📖 योजनाओं", "📣 मेरा चैनल", "💬 समीक्षा ", size=(2,)))


#back button 2
@user_router.message(F.text == '🔙Назад')
async def back2_ru(message: Message):
    await message.answer('Вы вернудись в предыдущее меню...', reply_markup=get_kbd("AI Анализ🤖", "🎲 Накрутка Удачи", "❌ Крестики Нолики", "🔙 Назад", size=(1,)))


@user_router.message(F.text == '🔙Back')
async def back1_en(message: Message):
    await message.answer('You are back to the previous menu...', reply_markup=get_kbd("AI Analysis🤖", "🎲 Cheat Luck", "❌ Tic Tac Toe", "🔙 Back", size=(1,)))


@user_router.message(F.text == '🔙पीछे')
async def back1_hi(message: Message):
    await message.answer('आप पिछले मेनू पर वापस आ गए हैं...', reply_markup=get_kbd("एआई विश्लेषण🤖", "🎲 धोखा किस्मत", "❌ टिक टीएसी को पैर की अंगुली", "🔙 पीछे", size=(1,)))


@user_router.message(StateFilter(None), F.text == '🎲 Накрутка Удачи')
async def nakr_ru(message: Message, state: FSMContext):
    await message.answer(text='Отправьте ID', reply_markup=get_kbd("📄Схема", "🔙Назад", size=(1,)))
    await state.set_state(ChooseScheme2.ai2_ru)


@user_router.message(ChooseScheme2.ai2_ru, F.text)
async def nakr2_ru(message: Message, state: FSMContext):
    await message.answer(text="Успешно ✅")
    await state.clear()


@user_router.message(ChooseScheme2.ai2_ru, F.text == '🔙Назад')
async def back_clear(state: FSMContext):
    await state.clear()


###
@user_router.message(StateFilter(None), F.text == '🎲 Cheat Luck')
async def nakr2_en(message: Message, state: FSMContext):
    await message.answer(text='Send ID', reply_markup=get_kbd("📄Scheme", "🔙Back", size=(1,)))
    await state.set_state(ChooseScheme2.ai2_en)


@user_router.message(ChooseScheme2.ai2_en, F.text)
async def nakr2e_en(message: Message, state: FSMContext):
    await message.answer(text="Successfully ✅")
    await state.clear()


@user_router.message(ChooseScheme2.ai2_en, F.text == '🔙Back')
async def back2_clear(state: FSMContext):
    await state.clear()


###
@user_router.message(StateFilter(None), F.text == '🎲 धोखा किस्मत')
async def nakr2_hi(message: Message, state: FSMContext):
    await message.answer(text='आईडी भेजें', reply_markup=get_kbd("📄योजना", "🔙पीछे", size=(1,)))
    await state.set_state(ChooseScheme2.ai2_hi)


@user_router.message(ChooseScheme2.ai2_hi, F.text)
async def nakr2e_hi(message: Message, state: FSMContext):
    await message.answer(text="सफलतापूर्वक ✅")
    await state.clear()


@user_router.message(ChooseScheme2.ai2_en, F.text == '🔙पीछे')
async def back3_clear(state: FSMContext):
    await state.clear()


#scheme but2
@user_router.message(F.text == '📄Схема')
async def schem_buttru2(message: Message):
    await message.answer('https://telegra.ph/ZenoAI-11-06')


@user_router.message(F.text == '📄Scheme')
async def schem_butten2(message: Message):
    await message.answer('https://telegra.ph/Luck-Bait-11-08')


@user_router.message(F.text == '📄योजना')
async def schem_butt2(message: Message):
    await message.answer('https://telegra.ph/%E0%A4%AD%E0%A4%97%E0%A4%AF-11-08')


#chanal button
@user_router.message(F.text == '📣 Мой канал')
async def chan_ru(message: Message):
    await message.answer("Выберите действие...", reply_markup=get_kbd("📣Мой канал", "🔙 Назад"))


@user_router.message(F.text == '📣 My chanal')
async def chan_en(message: Message):
    await message.answer("Select action...", reply_markup=get_kbd("📣My chanal", "🔙 Back"))


@user_router.message(F.text == '📣 मेरा चॅनल')
async def chan_hi(message: Message):
    await message.answer("कार्रवाई चुनें...", reply_markup=get_kbd("📣मेरा चॅनल", "🔙 वापस"))


#revies butt
@user_router.message(F.text == '💬 Отзывы')
async def rev_ru(message: Message):
    await message.answer('t.me/+pVj4tdAxxAxkMTNi')


@user_router.message(F.text == '💬 Reviews')
async def rev_en(message: Message):
    await message.answer('t.me/+QyxEwUJsxys4YWIy')


@user_router.message(F.text == '💬 समीक्षा')
async def rev_hi(message: Message):
    await message.answer('t.me/+66d42zOawb81YWNi')