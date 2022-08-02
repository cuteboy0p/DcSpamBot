#
# Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
#
# This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >
#
# All rights reserved.

import os
import sys
import asyncio
from datetime import datetime
from pyrogram import filters
from sys import version_info
from DcSpamBot import SUDO_USER, ALIVE_PIC, OWN_USERNAME, NAME
from pyrogram import Client
from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message
from time import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
keyboard = InlineKeyboardMarkup(
        [            
            [
                InlineKeyboardButton(text="Deploy ✔️", url="https://t.me/DeCodeUpdate"),
            ],
        ]
    )

@Client.on_message(filters.user(SUDO_USER) & filters.command(["alive"], [".", "!", "/"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))   
    reply_msg = f"**MADE IN 🇮🇳, MADE FOR 💜**\n"
    reply_msg += f"═══════════════════\n"
    reply_msg += f"🔸 `Python`: **{__python_version__}\n"
    reply_msg += f"🔹 `Ping `: **{delta_ping * 1000:.3f}ᵐˢ**\n"
    reply_msg += f"🔸 `Fork By`: **{NAME}**\n"
    reply_msg += f"🔹 `Bot Creator`: **{OWN_USERNAME}**\n"
    reply_msg += f"🔸 `PyroGram`: **{__pyro_version__}**\n"    
    reply_msg += f"🔹 `DeCoDe Uptime`: **{uptime}**\n"
    reply_msg += f"═══════════════════\n\n"
    reply_msg += f"**JOIN** [@TeamDeCoDe](https://t.me/decode_support) **FOR HELP**\n"
    await m.delete()
    await m.reply_photo(photo=f"{ALIVE_PIC}", caption=reply_msg,
               reply_markup=keyboard,                     
) 
