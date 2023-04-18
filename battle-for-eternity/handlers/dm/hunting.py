
# GAME MODE: HUNTING


#import random

from aiogram.types import Message, CallbackQuery,\
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,\
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

from _bot import dispatcher
from data import langpack
from states.hunting import HuntingGameSession



@dispatcher.message_handler(
    chat_type="private",
    text=langpack.M2_BUTTON__HUNTING
)
async def menu_hunting(update: Message):
    await update.answer(
        langpack.HUNTING__MESSAGE,
        reply_markup=None
    )
