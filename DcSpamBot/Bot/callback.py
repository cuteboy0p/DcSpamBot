#
# Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
#
# This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >
#
# All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message




@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
