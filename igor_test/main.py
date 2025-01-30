import asyncio
from config import bot,dp,db
from handlers import start


async def main():
    db.create_tables()
    dp.include_router(start.start_router)


    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())