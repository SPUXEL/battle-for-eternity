
# GAME MODE: HUNTING


import random

from aiogram.types import Message, CallbackQuery,\
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,\
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from _bot import dispatcher
from data import langpack
from utils import character
from utils.testcharacter import testcharacter
from utils.monsters import monsters


class HuntingGameSession(StatesGroup):
    combat_preparation = State()
    session = State()


async def _create_state_data(
    character: character.Character, game_mode: str
):
    global monsters

    if game_mode == "in_the_vicinity":
        return {
            "character": character,
            "character_health": None,
            "monster": random.choice(monsters.monsters)
        }

    if game_mode == "order":
        monsters = None
        return {
            "current_stage": 1,
            "total_stage": 1,
            "character": character,
            "monsters": monsters
        }


async def _keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button__hunting_in_the_vicinity = KeyboardButton(
        langpack.HUNTING__BUTTON__IN_THE_VICINITY
    )
    keyboard.add(button__hunting_in_the_vicinity)

    button__monster_order = KeyboardButton(
        langpack.HUNTING__BUTTON__MONSTER_ORDERS
    )
    keyboard.add(button__monster_order)

    button__back = KeyboardButton(
        langpack.BUTTON__TO_THE_MAIN_MENU
    )
    keyboard.add(button__back)

    return keyboard


@dispatcher.message_handler(
    chat_type="private",
    text=langpack.M2_BUTTON__HUNTING
)
async def menu_hunting(update: Message):
    await update.answer(
        langpack.HUNTING__MESSAGE,
        reply_markup=await _keyboard()
    )


@dispatcher.message_handler(
    chat_type="private",
    text=langpack.HUNTING__BUTTON__IN_THE_VICINITY
)
async def hunting_in_the_vicinity(update: Message, state: FSMContext):

    await HuntingGameSession().combat_preparation.set()
    state_data = await _create_state_data(testcharacter, game_mode="in_the_vicinity")
    await state.update_data(state_data)

    await update.answer(
        langpack.ASSIGNMENT_GAME_STATE,
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True
        ).add(
            KeyboardButton(
                langpack.HUNTING__BUTTON__START_HUNTING
            )
        )
    )

    await update.answer(
        langpack.PREPARING_FOR_THE_HUNT,
        reply_markup=None,
        disable_notification=True
    )
