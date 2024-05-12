import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from aiogram.client.session.aiohttp import AiohttpSession


# session = AiohttpSession(proxy="http://proxy.server:3128")
try:
    load_dotenv(dotenv_path="data/.env")
    dp = Dispatcher()
    bot = Bot(os.getenv("TOKEN"))

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
