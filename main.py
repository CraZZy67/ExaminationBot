from asyncio import run

from create_bot import bot, dp
from hand_user_side import router_for_user
from hand_admin_side import router_for_admin

dp.include_routers(router_for_user, router_for_admin)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    run(main())


