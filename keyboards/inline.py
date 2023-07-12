from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback.vegetables import VegetablesCallback
from callback.animals import AnimalsCallback
potatoes = InlineKeyboardButton(text='Картофель', callback_data=VegetablesCallback(vegetable='Картошка', count=3).pack())
carrots = InlineKeyboardButton(text='Морковка', callback_data=VegetablesCallback(vegetable='Морковка', count=2).pack())
cats = InlineKeyboardButton(text='Котов', callback_data=AnimalsCallback(animal='Кот', count=4).pack())
dogs = InlineKeyboardButton(text='Собак', callback_data=AnimalsCallback(animal='Собака', count=5).pack())
fish = InlineKeyboardButton(text='Рыб', callback_data=AnimalsCallback(animal='Рыба', count=1).pack())
owl = InlineKeyboardButton(text='Сов', callback_data=AnimalsCallback(animal='Сова', count=10).pack())
shop_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [potatoes, carrots]
])
cats_dogs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [cats, dogs],
    [fish, owl]
])