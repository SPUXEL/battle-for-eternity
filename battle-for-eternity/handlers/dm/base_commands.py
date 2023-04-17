
from aiogram.types import Message

from _bot import dispatcher
from data import langpack


@dispatcher.message_handler(commands=["start"])
async def command_start(update: Message):
    await update.answer(langpack.START__MESSAGE)
