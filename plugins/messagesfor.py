#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)



@pyrogram.Client.on_message(pyrogram.Filters.document | Filters.video)
async def getchat(bot, update):
    media = update.document or update.video
    name = media.file_name
    await bot.send_message(
      text=Translation.USER_TXT.format(name)
      chat_id=update.chat.id
    )
