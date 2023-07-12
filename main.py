import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message, CallbackQuery  # Тип сообщения

from callback.animals import AnimalsCallback
from callback.vegetables  import VegetablesCallback
from config import config  # Config
from keyboards.inline import cats_dogs_keyboard
from keyboards.inline import shop_keyboard
API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота



@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет, каких животных ты любишь больше",
                         reply_markup=cats_dogs_keyboard)
@dp.message(Command(commands=['shop']))
async def shop_command(message: Message):

    await message.answer("В нашем магазине продаются следующие товары:",
                         reply_markup=shop_keyboard)


@dp.callback_query(AnimalsCallback.filter())
async def handle_cats(query: CallbackQuery, callback_data: AnimalsCallback):
    await query.answer(f'Вы нажали на кнопку')
    await query.message.answer(f'Животное: {callback_data.animal}. Количество: {callback_data.count}')

@dp.callback_query(VegetablesCallback.filter())
async def veg(query: CallbackQuery, callback_data: VegetablesCallback):
    await query.answer("Совершенна покупка")
    await query.message.answer(f'Овощь: {callback_data.vegetable}. Количество: {callback_data.count}')


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
