# Infinity BOTs <https://t.me/Infinity_BOTs>
# @ImJanindu

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hello [{}](tg://user?id={}), I can download Songs!

Use /help to know how to use this bot

Owner @featzai
Other bots: @kxnekibot 
"""

help_text = """
My commands👇

- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
- Send youtube url to my pm for download it on audio format

Owner @featzai Report bugs: @ftfridaybot
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Kxnekibot", url="https://t.me/kxnekibot"
                    ),
                    InlineKeyboardButton(
                        text="Report bugs", url="https://t.me/ftfridaybot"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("JESongBot is online.")
idle()
