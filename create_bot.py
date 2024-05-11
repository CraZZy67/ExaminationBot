import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from aiogram.client.session.aiohttp import AiohttpSession


session = AiohttpSession(proxy="http://proxy.server:3128")
try:
    load_dotenv()
    dp = Dispatcher()
    bot = Bot(os.getenv("TOKEN"), session=session)

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
