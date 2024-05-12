from aiogram.filters import CommandStart, CommandObject
from aiogram.utils.markdown import link
from aiogram import Router, Bot
from aiogram.types import Message

import json


router_for_user = Router()

try:
    @router_for_user.message(CommandStart(deep_link=True))
    async def handling_link(message: Message, command: CommandObject, bot: Bot):
        args_list = command.args.split("s")

        with open("data/topics.json", "r", encoding="utf-8") as file:
            required_link = json.loads(file.read())[args_list[0]][int(args_list[1]) - 100]["link"]

        with open("data/channels.json", "r", encoding="utf-8") as file:
            chat_full_name = json.loads(file.read())[args_list[0]]["full_name"]

        with open("data/channels.json", "r", encoding="utf-8") as file:
            chat_id = json.loads(file.read())[args_list[0]]["id"]
            examination = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)

        hyper_text = link("Я ПОДПИСАЛСЯ", f"https://t.me/examination1_bot?start={command.args}")
        if examination.status == "left":
            await message.answer("Здравствуйте, это бот проверки на спам пользователей, "
                                 f"чтобы дочитать продолжение, подпишитесь на канал - https://t.me/{chat_full_name}. "
                                 f"После подписки нажмите на эту кнопку: \n\n{hyper_text}", parse_mode="Markdown")
        else:
            await message.answer(f"Вы успешно прошли проверку. Благодарим за подписку! "
                                 f"Продолжение рассказа: {required_link}")


    @router_for_user.message(CommandStart(ignore_case=True))
    async def handling_start(message: Message):
        await message.answer("Для использования бота перейдите по ссылке в публикации.")

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
