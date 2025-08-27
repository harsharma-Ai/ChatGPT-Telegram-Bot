import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Handlers
@router.message(F.text.in_(['start', 'help']))
async def send_welcome(message: Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram V3.")

@router.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)

# Main entry point
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())