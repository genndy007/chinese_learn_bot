from aiogram import types


async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Thanks for using bot, {full_name}")
