from aiogram.utils.keyboard import InlineKeyboardBuilder


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

        builder.button(text="Удалить канал", callback_data="delete_chanel")
        builder.button(text="Добавить канал", callback_data="add_channel")
        builder.button(text="Назад", callback_data="back_to_menu")
        builder.adjust(2, 1)

        return builder.as_markup()
