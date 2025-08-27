"""
Author: IKKO_BOT
"""

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor , types
import openai

class Reference:
    """
    A class to store the previous rersponses from the chatGPT API.
    """
    def __init__(self) -> None:
        self.response =""

# Load env variables
load_dotenv()

# set up OpenAI API key.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a reference object to store the previous response
reference = Reference()

# Bot token can be obtained via https://t.me/BotFather
Token = os.getenv("TOKEN")

# Model used in chatGPT
MODEL_NAME ="gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """
    A function to clear the previous conversation and context.
    """
    reference.response =""

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("Cleared the past conmtext and chat Bro..!")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi there, I'm IKKO bot powered by chatGPT! Please follow these commands -
    /start - to start the conversation 
    /clear - to clear the past converstion and context.
    /help - to get this help menu.
    I hope this helps.
    """

    await message.reply(help_command)

@dispatcher.message_handler(help_command)
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using cahtGPT API KEY
    """
    print(f">>> USER: \n{message.text}")
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response}, # here role means bot
            {"role":"user", "content": message.text} # our new question
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)


if __name__ == '__main__':
    print("Starting...")
    executor.start_polling(dispatcher)
    print("stopped")
