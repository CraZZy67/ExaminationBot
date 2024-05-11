from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

import json

from callback_factory import CallbackChannels
from keyboard import *
from support_func import *
from fsm import AddChannel, DelChannel

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
async def handling_back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text("Выберите действие.", reply_markup=kb_admin())


@router_for_admin.callback_query(F.data == "add_channel")
async def handling_first_state(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddChannel.id)
    await callback.message.answer("Перешлите любой пост из канала который хотите добавить.")
    await callback.message.answer("И не забудьте добавит бота в администраторы канала!")
    await callback.answer()


@router_for_admin.message(AddChannel.id)
async def catch_id_state(message: Message, state: FSMContext):
    data = await state.update_data(id=message.forward_origin.chat.id)
    chat = message.forward_origin.chat.username
    AddChannel.add_json_channels(data["id"], chat)
    await state.clear()
    await message.answer("Канал добавлен!")
    await message.answer("Выберите действие.", reply_markup=kb_admin())


@router_for_admin.callback_query(F.data == "delete_chanel")
async def handling_first_state_del(callback: CallbackQuery, state: FSMContext):
    await state.set_state(DelChannel.number)
    await callback.message.answer("Введите номер канала который хотите удалить.")
    await callback.answer()


@router_for_admin.message(DelChannel.number)
async def catch_number_state(message: Message, state: FSMContext):
    data = await state.update_data(number=message.text)
    DelChannel.del_json_channel(data["number"])
    await state.clear()
    await message.answer("Канал удален!")
    await message.answer("Выберите действие.", reply_markup=kb_admin())


@router_for_admin.callback_query(F.data == "topics_list")
async def handling_topics_list(callback: CallbackQuery):
    if exam_len("channels"):
        await callback.message.edit_text("Выберите канал с нужными постами.", reply_markup=kb_channels_buttons())
    else:
        await callback.message.edit_text("Список каналов пуст.", reply_markup=kb_channels_buttons("empty"))


@router_for_admin.callback_query(CallbackChannels.filter(F.base == "b"))
async def handling_channels_buttons(callback: CallbackQuery, callback_data: CallbackChannels):
    if len_topics_current_channel(callback_data.number):
        await callback.message.edit_text(list_for_topics(callback_data.number), reply_markup=kb_list_topics())
    else:
        await callback.message.edit_text("Список постов этого канала пуст.", reply_markup=kb_list_topics("empty"))

