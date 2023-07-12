from aiogram.filters.callback_data import CallbackData

class VegetablesCallback(CallbackData, prefix='vegetables'):
    vegetable: str
    count: int