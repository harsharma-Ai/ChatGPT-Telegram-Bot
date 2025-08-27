""""
Author: NONAME    

for the older version of aiogram v2 or below
"""

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai

class Reference:
    def __init__(self):
        self.response = ""

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create reference object
reference = Reference()

# Telegram Bot token
TOKEN = os.getenv("TOKEN")

# ChatGPT model
MODEL_NAME = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    reference.response = ""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    clear_past()
    await message.reply("Hey, I'm IKKO BOT powered by AI and created by Noname..!")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
Hi there, I'm IKKO bot based on AI. Please follow these commands:
/start - to start the conversation.
/clear - to clear the past conversation and context.
/help - to get this help menu.
I HOPE THIS HELPS.
"""
    await message.reply(help_command)

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("Cleared the past context and chat Bro..!")

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
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
    await bot.send_message(chat_id=message.chat.id, text=reference.response)

if __name__ == '__main__':
    print("Starting..!")
    executor.start_polling(dispatcher)
    print("Stopped")