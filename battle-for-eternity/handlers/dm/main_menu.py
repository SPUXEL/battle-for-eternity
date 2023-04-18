
from aiogram.types import Message,\
    ReplyKeyboardMarkup, KeyboardButton

from _bot import dispatcher
from data import langpack


async def _keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button__hunting = KeyboardButton(
        langpack.M2_BUTTON__HUNTING
    )
    keyboard.add(button__hunting)

    button__character = KeyboardButton(
        langpack.M2_BUTTON__CHARACTER
    )
    keyboard.add(button__character)

    return keyboard


@dispatcher.message_handler(
    chat_type="private",
    commands=["menu"]
)
async def main_menu(update: Message):
    await update.answer(
        langpack.M2_MESSAGE,
        reply_markup=await _keyboard()
    )


@dispatcher.message_handler(
    chat_type="private",
    text=langpack.BUTTON__TO_THE_MAIN_MENU
)
async def back_to_the_main_menu(update: Message):
    await main_menu(update)
