import logging

from aiogram import Bot, Dispatcher, types, executor
from loguru import logger

from src.constants import BOT_TOKEN
from src.commands import cmd_start
from src.uvloop import run_uvloop


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(cmd_start, commands="start")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
