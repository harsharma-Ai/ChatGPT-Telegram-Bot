"""
Author: NONAME

-> this module conatins the implementation of a telegram bot that uses the OpemAi chatGPT API
   to generate responses to users.

   usage:-
          1. Set up a telegram bot and obtain its token.
          2. Set up an OpenAi account and obtain an API key.
          3. Set the environment var. "Token" and "Openai_api_key"
             to the bot token and OpenAI API key, respectively.
          4. Run the script to start the bot.

    -> Note: this implementation uses the aiogram, openai library to interact with the Telegram API 
             and the Openai API, respectively.

    -> E.g;  $ python chatgpt.py

    """

import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
import openai

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Telegram Bot token
TOKEN = os.getenv("TOKEN")

# ChatGPT model
MODEL_NAME = "gpt-3.5-turbo"

# Create reference object
class Reference:
    def __init__(self):
        self.response = ""

reference = Reference()

# Initialize bot and dispatcher
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Create router
router = Router()
dp.include_router(router)

# Clear context
def clear_past():
    reference.response = ""

# Handlers
@router.message(F.text =="/start")
async def welcome(message: Message):
    clear_past()
    await message.answer("Hey, I'm IKKO BOT powered by AI and created by Noname..!")

@router.message(F.text =="/help")
async def helper(message: Message):
    help_command = """
Hi there, I'm IKKO bot based on AI. Please follow these commands:
/start - to start the conversation.
/clear - to clear the past conversation and context.
/help - to get this help menu.
I HOPE THIS HELPS.
"""
    await message.answer(help_command)

@router.message(F.text == "/clear")
async def clear(message: Message):
    clear_past()
    await message.answer("Cleared the past context and chat Bro..!")

@router.message()
async def chatgpt(message: Message):
    print(f">>> USER:\n{message.text}")
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> ChatGPT:\n{reference.response}")
    await message.answer(reference.response)

# Main entry
async def main():
    print("Starting..!")
    await dp.start_polling(bot)
    print("Stopped")

if __name__ == "__main__":
    asyncio.run(main())