import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv


load_dotenv()
dp = Dispatcher()
bot = Bot(os.getenv("TOKEN"))
