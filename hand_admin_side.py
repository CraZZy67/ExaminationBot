from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

import json

from keyboard import kb_admin, kb_channels_list
from support_func import pars_json_to_list

router_for_admin = Router()
valid_users = [5617141084, 1162899410]


@router_for_admin.message(F.text == "/admin")
async def handling_admin(message: Message):
    if message.from_user.id in valid_users:
        await message.answer("Выберите действие.", reply_markup=kb_admin())


@router_for_admin.callback_query(F.data == "channels_list")
async def handling_channels_list(callback: CallbackQuery):
    with open("channels.json", "r", encoding="utf-8") as file:
        channels = json.loads(file.read())
    if len(channels) > 0:
        formated_str = pars_json_to_list(channels)
        await callback.message.edit_text(formated_str, reply_markup=kb_channels_list())
    else:
        await callback.message.edit_text("Список каналов пуст.", reply_markup=kb_channels_list(mode="empty"))


@router_for_admin.callback_query(F.data == "back_to_menu")
async def handling_channels_list(callback: CallbackQuery):
    await callback.message.edit_text("Выберите действие.", reply_markup=kb_admin())