from aiogram.filters import CommandStart, CommandObject
from aiogram import Router, Bot
from aiogram.types import Message

from keyboard import kb_user
from users_data_func import add_user

from support_func import examination_json_inf


router_for_user = Router()

try:
    @router_for_user.message(CommandStart(deep_link=True))
    async def handling_link(message: Message, command: CommandObject, bot: Bot):
        args_list = command.args.split("s")
        dict_inf = examination_json_inf(args_list)

        examination = await bot.get_chat_member(dict_inf["id"], message.from_user.id)

        if examination.status == "left":
            await message.answer(dict_inf["strings"][0],
                                 reply_markup=kb_user(f'https://t.me/examination1_bot?start={command.args}'))
        else:
            await message.answer(dict_inf["strings"][1])

        username = "None" if message.from_user.username is None else message.from_user.username
        add_user([username, message.from_user.first_name, message.from_user.id])

    @router_for_user.message(CommandStart(ignore_case=True))
    async def handling_start(message: Message):
        await message.answer("Для использования бота перейдите по ссылке в публикации.")

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
