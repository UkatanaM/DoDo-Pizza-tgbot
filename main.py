import asyncio 
from aiogram import Bot, Dispatcher
from config import settings

async def main():
    bot = Bot(token=settings.bot_token.get_secret_value())
    dp = Dispatcher()

    print('Bot is running...')
    await dp.start_polling(bot)
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt):
        print('Bot stopped.')
