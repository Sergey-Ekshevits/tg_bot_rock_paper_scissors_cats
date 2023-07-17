import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.set_menu import set_main_menu

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Создаем асинхронную функцию
# async def set_main_menu(bot: Bot):
#
#     # Создаем список с командами и их описанием для кнопки menu
#     main_menu_commands = [
#         BotCommand(command='/help',
#                    description='Справка по работе бота'),
#         BotCommand(command='/support',
#                    description='Поддержка'),
#         BotCommand(command='/contacts',
#                    description='Другие способы связи'),
#         BotCommand(command='/payments',
#                    description='Платежи')]
#
#     await bot.set_my_commands(main_menu_commands)
# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config('.env')

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, 
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # async with bot.session:
        # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await set_main_menu(bot)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
