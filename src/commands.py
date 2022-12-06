from aiogram import types


async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Thanks for using bot, {full_name}")


async def cmd_word_groups(message: types.Message):
    await message.answer("Here are all your groups")


async def cmd_add_group(message: types.Message):
    await message.answer("Adding new group")


async def cmd_add_word(message: types.Message):
    await message.answer("Adding new word")


CMD_NAME_TO_FUNC = {
    "start": cmd_start,
    "word_groups": cmd_word_groups,
    "add_group": cmd_add_group,
    "add_word": cmd_add_word,
}
