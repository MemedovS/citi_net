import asyncio
import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config.config import bot
from siti_bot.handlers import router
#from siti_bot.test import router


# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def main():
    # Инициализация диспетчера с хранилищем памяти
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)  # Подключение роутеров с хендлерами
    await bot.delete_webhook(drop_pending_updates=True)  # Сбрасываем обновления

    # Запуск long-polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())  # Запуск асинхронного приложения
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")
