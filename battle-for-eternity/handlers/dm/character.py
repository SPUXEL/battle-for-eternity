
from aiogram.types import Message,\
    ReplyKeyboardMarkup, KeyboardButton

from _bot import dispatcher
from data import langpack
from utils.testcharacter import testcharacter


async def _keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button__back = KeyboardButton(
        langpack.BUTTON__TO_THE_MAIN_MENU
    )
    keyboard.add(button__back)

    return keyboard


@dispatcher.message_handler(
    chat_type="private",
    text=langpack.M2_BUTTON__CHARACTER
)
async def character(update: Message):
    await update.answer(
        langpack.CHARACTER__MESSAGE.\
            replace("character-level", str(testcharacter.level.level)).\
            replace("character-experience", str(testcharacter.level.experience)).\
            replace("character-damage", str(testcharacter.base_characteristics.damage)).\
            replace("character-health", str(testcharacter.base_characteristics.health)).\
            replace("character-armor", str(testcharacter.base_characteristics.armor)).\
            replace("weapon-name", str(testcharacter.slots.weapon.name)).\
            replace("weapon-value", str(testcharacter.slots.weapon.value)).\
            replace("armor-name", str(testcharacter.slots.armor.name)).\
            replace("armor-value", str(testcharacter.slots.armor.value)),
        reply_markup=await _keyboard()
    )
