
# STATE: HUNTING


from aiogram.dispatcher.filters.state import StatesGroup, State


class HuntingGameSession(StatesGroup):
    quick_combat_preparation = State()
    quick_session = State()
