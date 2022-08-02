from pyrogram.types import Message
import asyncio
import asyncio
from pyrogram import filters, Client
from DcSpamBot import SUDO_USER as sudo_user

@Client.on_message(filters.user(sudo_user) & filters.command(["leave", "remove"], [".", "!", "/"]))
async def leave(client: Client, message: Message):
    sex  = await message.reply_text("<b>Leaving ChatID That You Provided!!</b>")
    chatid = message.command[1]
    await client.leave_chat(chatid) 
