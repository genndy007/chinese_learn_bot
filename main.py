import os

from aiogram import Bot, Dispatcher, executor, types
from loguru import logger

from src.constants import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def main(message: types.Message):
    await message.reply("Start or help from Chinese Learn Bot")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Dunno what to say")


if __name__ == "__main__":
    logger.info("Bot started!")
    executor.start_polling(dp, skip_updates=True)
