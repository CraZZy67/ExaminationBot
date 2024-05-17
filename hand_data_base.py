from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from users_data_func import counting_users, clear_db
from keyboard import kb_actions_db


router_for_db = Router()


@router_for_db.message(F.text == "/users")
async def users_actions(message: Message):
    await message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                         reply_markup=kb_actions_db())


@router_for_db.callback_query(F.data == "clear_data_base")
async def clear_data_base(callback: CallbackQuery):
    clear_db()
    await callback.message.answer("База данных отчищена")
    await callback.answer()
    await callback.message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                                  reply_markup=kb_actions_db())
