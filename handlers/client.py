from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Started', reply_markup=kb_client)
    except:
        await message.reply('Write to bot directly https://t.me/pizzaLizardBot')


async def work_time(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Круглосуточно каждый день!')
    except:
        await message.reply('Write to bot directly https://t.me/pizzaLizardBot')


async def office_address(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вольная, 30', reply_markup=ReplyKeyboardRemove())
    except:
        await message.reply('Write to bot directly https://t.me/pizzaLizardBot')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(work_time, commands=['Режим_работы'])
    dp.register_message_handler(office_address, commands=['Адрес'])