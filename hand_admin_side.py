from aiogram.types import Message, CallbackQuery, Chat
from aiogram.utils.deep_linking import create_start_link
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from keyboard import *
from support_func import *
from fsm import AddChannel, AddTopic
try:
    router_for_admin = Router()
    valid_users = [5617141084, 1162899410, 5919006420]
    current_channel = str()


    @router_for_admin.message(F.text == "/admin")
    async def handling_admin(message: Message):
        if message.from_user.id in valid_users:
            await message.answer("Выберите действие.", reply_markup=kb_admin())


    @router_for_admin.callback_query(F.data == "channels_list")
    async def handling_channels_list(callback: CallbackQuery):
        with open("data/channels.json", "r", encoding="utf-8") as file:
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


    @router_for_admin.message(Command("cancel"))
    @router_for_admin.message(F.text.casefold() == "cancel")
    async def cancel_handler(message: Message, state: FSMContext):
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.clear()
        await message.answer("Совершен выход")
        await message.answer("Выберите действие.", reply_markup=kb_admin())


    @router_for_admin.message(AddChannel.id)
    async def catch_id_state(message: Message, state: FSMContext):
        data = await state.update_data(id=message.forward_origin.chat.id)
        chat = message.forward_origin.chat.username
        AddChannel.add_json_channels(data["id"], chat)
        await state.clear()
        await message.answer("Канал добавлен!")
        await message.answer("Выберите действие.", reply_markup=kb_admin())


    @router_for_admin.callback_query(F.data == "delete_channels")
    async def handling_del(callback: CallbackQuery):
        with open("data/channels.json", "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)

        with open("data/topics.json", "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)

        await callback.message.edit_text("Выберите действие.", reply_markup=kb_admin())
        await callback.message.answer("Все каналы и посты отчищены!")


    @router_for_admin.callback_query(F.data == "topics_list")
    async def handling_topics_list(callback: CallbackQuery):
        if exam_len("channels"):
            await callback.message.edit_text("Выберите канал с нужными постами.", reply_markup=kb_channels_buttons())
        else:
            await callback.message.edit_text("Список каналов пуст.", reply_markup=kb_channels_buttons("empty"))


    @router_for_admin.callback_query(CallbackChannels.filter(F.base == "b"))
    async def handling_channels_buttons(callback: CallbackQuery, callback_data: CallbackChannels):
        global current_channel
        current_channel = callback_data.number

        if len_topics_current_channel(callback_data.number):
            await callback.message.edit_text(list_for_topics(callback_data.number), reply_markup=kb_list_topics(),
                                             disable_web_page_preview=True)
        else:
            await callback.message.edit_text("Список постов этого канала пуст.", reply_markup=kb_list_topics())


    @router_for_admin.callback_query(F.data == "add_topic")
    async def handling_add_topic(callback: CallbackQuery, state: FSMContext):
        await state.set_state(AddTopic.link)
        await callback.message.answer("Введите ссылку для продолжения поста")
        await callback.answer()


    @router_for_admin.message(AddTopic.link)
    async def catch_state_link(message: Message, state: FSMContext, bot: Bot):
        global current_channel
        data = await state.update_data(link=message.text)
        number_for_link = AddTopic.add_json_topic(link=data["link"], number_channel=current_channel)
        link = await create_start_link(bot, f"{current_channel}s{number_for_link}")
        await state.clear()
        await message.answer("Пост добавлен!")
        await message.answer(f"Индивидуальная ссылка для поста: {link}")
        await message.answer("Выберите действие.", reply_markup=kb_admin())

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
