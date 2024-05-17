from asyncio import run

from create_bot import bot, dp
from hand_user_side import router_for_user
from hand_admin_side import router_for_admin
from hand_data_base import router_for_db


dp.include_routers(router_for_user, router_for_admin, router_for_db)

try:
    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        print("Бот запущен!")
        run(main())

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")


