
from aiogram.types import Message

from _bot import dispatcher
from data import langpack


@dispatcher.message_handler(commands=["start"])
async def command_start(update: Message):
    await update.answer(
        langpack.START__MESSAGE1.replace(
            "user-name", update.from_user.full_name
        )
    )
    await update.answer(
        langpack.START__MESSAGE2,
        disable_notification=True
    )
    await update.answer(
        langpack.START__MESSAGE3,
        disable_notification=True
    )
