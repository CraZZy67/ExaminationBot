from aiogram.utils.keyboard import InlineKeyboardBuilder

import json

from callback_factory import CallbackChannels
from users_data_func import counting_users


def kb_admin():
    builder = InlineKeyboardBuilder()

    builder.button(text="Список каналов", callback_data="channels_list")
    builder.button(text="Список постов", callback_data="topics_list")

    return builder.as_markup()


def kb_channels_list(mode: str | None = None):
    if mode == "empty":
        builder = InlineKeyboardBuilder()

        builder.button(text="Добавить канал", callback_data="add_channel")
        builder.button(text="Назад", callback_data="back_to_menu")

        return builder.as_markup()
    else:
        builder = InlineKeyboardBuilder()

        builder.button(text="Отчистить все каналы и посты!", callback_data="delete_channels")
        builder.button(text="Добавить канал", callback_data="add_channel")
        builder.button(text="Назад", callback_data="back_to_menu")
        builder.adjust(2, 1)

        return builder.as_markup()


def kb_channels_buttons(mode: str | None = None):
    if mode == "empty":
        builder = InlineKeyboardBuilder()

        builder.button(text="Назад", callback_data="back_to_menu")
        return builder.as_markup()
    else:
        with open("data/channels.json", "r", encoding="utf-8") as file:
            json_dict = json.loads(file.read())

        builder = InlineKeyboardBuilder()
        for k, v in json_dict.items():
            builder.button(text=v["full_name"], callback_data=CallbackChannels(name=v["full_name"], number=k, base="b"))

        builder.button(text="Назад", callback_data="back_to_menu")
        builder.adjust(2, repeat=True)
        return builder.as_markup()


def kb_list_topics():

    builder = InlineKeyboardBuilder()

    builder.button(text="Добавить пост", callback_data="add_topic")
    builder.button(text="Назад", callback_data="back_to_menu")

    return builder.as_markup()


def kb_user(url: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Я подписался ✅", url=url)
    return builder.as_markup()


def kb_actions_db():
    builder = InlineKeyboardBuilder()

    if counting_users() > 0:
        builder.button(text="Отчистить базу данных", callback_data="clear_data_base")
        builder.button(text="Сообщение пользователям", callback_data="message_users")

    return builder.as_markup()
