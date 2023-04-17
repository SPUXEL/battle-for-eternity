
from aiogram import executor

from _bot import dispatcher
import handlers


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dispatcher, skip_updates=True
    )
