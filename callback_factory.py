from aiogram.filters.callback_data import CallbackData


class CallbackChannels(CallbackData, prefix="channels"):
    number: str
    name: str
