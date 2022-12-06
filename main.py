import logging

from aiogram import Bot, Dispatcher, types, executor
from loguru import logger

from src.constants import BOT_TOKEN
from src.commands import CMD_NAME_TO_FUNC
from src.uvloop import run_uvloop


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

for cmd_name, cmd_func in CMD_NAME_TO_FUNC.items():
    dp.register_message_handler(cmd_func, commands=cmd_name)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
