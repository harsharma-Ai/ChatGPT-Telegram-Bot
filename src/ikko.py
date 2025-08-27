"""
This is a Ikko bot.
It respond to any incoming messages.
"""

import logging

from aiogram import Bot, Dispatcher , executor, types

API_TOKEN = '8220974162:AAEXP6Zz4ugDkbW2wioN9M2LDSKfiebRetk'

#Configuration logging 

logging.basicConfig(level=loggging.INFO)

#Initialize bot and dispatcher
bot= Bot(token=API_TOKEN)
dp= Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when users sends 'start' or '/help' command 
    """
    await message.reply("Hey...!\n I'm IKKO_Bot!\n Powered by aiogram.")

@dp.message_handler()
async def ikko(message: types.Message):
    await message.answer(message.text)

if __name__=='__main__':
     executor.start_polling(dp,skip_updates)