from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.methods import GetChatMember


router_first = Router()


@router_first.message(CommandStart(ignore_case=True))
async def handling_start(message: Message, bot: Bot):
    await message.answer("Hello World")
    examination = await bot.get_chat_member(chat_id=-1002067770316, user_id=message.from_user.id)
    await message.answer(f"{examination.status == "left"}")

