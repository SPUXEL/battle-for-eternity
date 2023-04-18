
from aiogram.types import Message

from _bot import dispatcher
from data import langpack


@dispatcher.message_handler(
    chat_type="private",
    text=langpack.M2_BUTTON__CHARACTER
)
async def character(update: Message):
    await update.answer(
        langpack.CHARACTER__MESSAGE
    )
