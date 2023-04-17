
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


storage = MemoryStorage()
bot = Bot(
    token=config.TG_TOKEN, parse_mode=ParseMode.HTML
)
dispatcher = Dispatcher(bot, storage=storage)
