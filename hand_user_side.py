from aiogram.filters import CommandStart, CommandObject
from aiogram import Router, Bot
from aiogram.types import Message

import json


router_for_user = Router()


@router_for_user.message(CommandStart(deep_link=True))
async def handling_link(message: Message, command: CommandObject, bot: Bot):
    args_list = command.args.split("s")

    with open("data.json", "r", encoding="utf-8") as f:
        required_link = json.loads(f.read())[args_list[0]][args_list[1]]

    with open("id.json", "r", encoding="utf-8") as f:
        chat_id = json.loads(f.read())[args_list[0]]
        examination = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)

    if examination.status == "left":
        await message.answer("Перед тем как вы посмотрите продолжение вам нужно подписаться на канал!")
    else:
        await message.answer(f"Вот продолжение публикации: {required_link}")


@router_for_user.message(CommandStart(ignore_case=True))
async def handling_start(message: Message):
    await message.answer("Для использования бота перейдите по ссылке в публикации.")
