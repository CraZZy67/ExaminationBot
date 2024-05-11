import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv

try:
    load_dotenv()
    dp = Dispatcher()
    bot = Bot(os.getenv("TOKEN"))

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
