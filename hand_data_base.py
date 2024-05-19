import csv

from aiogram.types import Message, CallbackQuery
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramForbiddenError

from users_data_func import counting_users, clear_db
from keyboard import kb_actions_db
from fsm import SendMessage

try:
    router_for_db = Router()
    valid_users = [5617141084, 1162899410, 5919006420]

    @router_for_db.message(F.text == "/users")
    async def users_actions(message: Message):
        if message.from_user.id in valid_users:
            await message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                                 reply_markup=kb_actions_db())


    @router_for_db.callback_query(F.data == "clear_data_base")
    async def clear_data_base(callback: CallbackQuery):
        clear_db()
        await callback.message.answer("База данных отчищена")
        await callback.answer()
        await callback.message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                                      reply_markup=kb_actions_db())


    @router_for_db.callback_query(F.data == "message_users")
    async def set_state_message(callback: CallbackQuery, state: FSMContext):
        await state.set_state(SendMessage.message)
        await callback.message.answer("Введите одним сообщением что хотите отправить.")
        await callback.answer()


    @router_for_db.message(SendMessage.message)
    async def catch_message(message: Message, state: FSMContext, bot: Bot):
        data = await state.update_data(message=message.text)
        banned_users = 0
        with open("data/users_data.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            reader.__next__()
            for i in reader:
                try:
                    await bot.send_message(chat_id=i[2], text=data["message"],
                                           parse_mode="HTML")

                except TelegramForbiddenError:
                    banned_users += 1
                    print(f"Невозможно отправить сообщение пользователю: {banned_users}")

        await state.clear()
        await message.answer("Сообщение отправлено!")
        await message.answer(f"Пользователей с заблокированным ботом: {banned_users}")
        await message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                             reply_markup=kb_actions_db())

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
