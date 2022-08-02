#
# Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
#
# This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >
#
# All rights reserved.

import asyncio
from pyrogram import idle
from DcSpamBot import bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, LOGGER

async def main():
    await bot1.start() 
    await bot1.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot2.start() 
    await bot2.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot3.start() 
    await bot3.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot4.start() 
    await bot4.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot5.start() 
    await bot5.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot6.start() 
    await bot6.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot7.start() 
    await bot7.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot8.start() 
    await bot8.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot9.start() 
    await bot9.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await bot10.start() 
    await bot10.send_message(
            LOGGER, 
            "<b> Congrats!! DcSpamBot Started Successfully!</b>", 
        ) 
    await idle()




'''SPAM BOT LOGS'''

botlogs = "Yeah Your Spam Bot Deploying Successfully, "
team = "© TeamDeCode"
c = botlogs + team
print(c)


    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
