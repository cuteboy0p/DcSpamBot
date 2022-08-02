#
# Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
#
# This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >
#
# All rights reserved.

from config import *
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# VARS IN BOTH CLIENT

API_ID = API_ID
API_HASH = API_HASH
SUDO_USER = SUDO_USERS
LOGGER = LOGGER
OWNER = OWNER
ALIVE_PIC = ALIVE_PIC

# VARS FOR BOT SPAMBOT

TOKEN1 = TOKEN1
TOKEN2 = TOKEN2
TOKEN3 = TOKEN3
TOKEN4 = TOKEN4
TOKEN5 = TOKEN5 
TOKEN6 = TOKEN6
TOKEN7 = TOKEN7
TOKEN8 = TOKEN8
TOKEN9 = TOKEN9
TOKEN10 = TOKEN10

if ALIVE_PIC:
    ALIVE_PIC = ALIVE_PIC
else: 
    ALIVE_PIC = "https://telegra.ph/file/a9b56319322553da4b240.jpg"

if not TOKEN1:
    logging.error("No Token Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

# FOR  SPAMBOT START

if TOKEN1:
    print("[INFO] TOKEN1 Found!! Booting SpamBot Client1... ") 
    bot1 = Client(":memory:", bot_token=TOKEN1, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot1 = None

if TOKEN2:
    print("[INFO] TOKEN2 Found!! Booting SpamBot Client3... ") 
    bot2 = Client(":memory:", bot_token=TOKEN2, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot2 = None


if TOKEN3:
    print("[INFO] TOKEN3 Found!! Booting SpamBot Client3... ") 
    bot3 = Client(":memory:", bot_token=TOKEN3, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot3 = None

if TOKEN4:
    print("[INFO] TOKEN4 Found!! Booting SpamBot Client4... ") 
    bot4 = Client(":memory:", bot_token=TOKEN4, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot4 = None

if TOKEN5:
    print("[INFO] TOKEN5 Found!! Booting SpamBot Client5... ") 
    bot5 = Client(":memory:", bot_token=TOKEN5, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot5 = None

if TOKEN6:
    print("[INFO] TOKEN6 Found!! Booting SpamBot Client6... ") 
    bot6 = Client(":memory:", bot_token=TOKEN6, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot6 = None

if TOKEN7:
    print("[INFO] TOKEN7 Found!! Booting SpamBot Client7... ") 
    bot7 = Client(":memory:", bot_token=TOKEN7, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot7 = None

if TOKEN8:
    print("[INFO] TOKEN8 Found!! Booting SpamBot Client8... ") 
    bot8 = Client(":memory:", bot_token=TOKEN8, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot8 = None

if TOKEN9:
    print("[INFO] TOKEN9 Found!! Booting SpamBot Client9... ") 
    bot9 = Client(":memory:", bot_token=TOKEN9, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot9 = None

if TOKEN10:
    print("[INFO] TOKEN10 Found!! Booting SpamBot Client10... ") 
    bot10 = Client(":memory:", bot_token=TOKEN10, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="DcSpam.Bot"))
else:
    bot10 = None



scheduler = AsyncIOScheduler()
START_TIME = datetime.now()
