from aiogram import types, Dispatcher
import json, string


# @dp.message_handler()
async def censored(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Censored!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(censored)