#
# Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
#
# This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >
#
# All rights reserved.

from pyrogram.types import Message
import asyncio
import asyncio
from pyrogram import filters, Client
from DcSpamBot.Data.Cache import RAID, PROGROUPS
from DcSpamBot import SUDO_USER as sudo_user

# DELAY SPAM HANDLER
@Client.on_message(filters.user(sudo_user) & filters.command(["delspam", "delayspam"], [".", "!", "/"]))
async def statspam(client: Client, message: Message):
    sex  = await message.reply_text("Usage:\n /delspam 10 MADRHARCHOD")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    for i in range(quantity):
        await sex .delete()
        msg = await client.send_message(message.chat.id, spam_text)       
        await asyncio.sleep(0.1)

# SPAM. HANDLER
@Client.on_message(filters.user(sudo_user) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def sspam(client: Client, message: Message):
    sex  = await message.reply_text("⚡ Usage:\n /spam 10 LODA ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await sex .delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)

#FASTSPAM HANDLER
@Client.on_message(filters.user(sudo_user) & filters.command(["fastspam"], [".", "!", "/"]))
async def fastspam(client: Client, message: Message):
    sex  = await message.reply_text("⚡ Usage:\n /fastspam 10 LODA ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.002)
        return
    
    for _ in range(quantity):
        await sex .delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)


#SLOWSPAM HANDLER
@Client.on_message(filters.user(sudo_user) & filters.command(["slowspam"], [".", "!", "/"]))
async def slowspam(client: Client, message: Message):
    sex = await message.reply_text("⚡ Usage:\n /slowspam 10 LODA ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await sex.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)






#STICKERSPAM HANDLER
@Client.on_message(filters.user(sudo_user) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if LODA .chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)
