from asyncio import run

from create_bot import bot, dp
from handlers import router_first

dp.include_routers(router_first)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    run(main())


