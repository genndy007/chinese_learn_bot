import logging

from aiogram import Bot, Dispatcher, types
from loguru import logger

from src.constants import BOT_TOKEN
from src.uvloop import run_uvloop

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(commands=["start"])
async def start(message: types.Message):
    full_user_name = message.from_user.full_name
    user_tag = message.from_user.username
    answer_string = (
        f"Hello, {full_user_name}, tag {user_tag}, thanks for choosing our bot!"
    )
    await message.answer(answer_string)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Bot started!")
    run_uvloop(main())
