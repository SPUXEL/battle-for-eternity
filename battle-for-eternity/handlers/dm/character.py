
from aiogram.types import Message

from _bot import dispatcher
from data import langpack
from utils.test_character import character as _character


@dispatcher.message_handler(
    chat_type="private",
    text=langpack.M2_BUTTON__CHARACTER
)
async def character(update: Message):
    await update.answer(
        langpack.CHARACTER__MESSAGE.\
            replace("character-level", str(_character.level.level)).\
            replace("character-experience", str(_character.level.experience)).\
            replace("character-damage", str(_character.base_characteristics.damage)).\
            replace("character-health", str(_character.base_characteristics.health)).\
            replace("character-armor", str(_character.base_characteristics.armor)).\
            replace("weapon-name", str(_character.slots.weapon.name)).\
            replace("weapon-value", str(_character.slots.weapon.value)).\
            replace("armor-name", str(_character.slots.armor.name)).\
            replace("armor-value", str(_character.slots.armor.value))
    )
