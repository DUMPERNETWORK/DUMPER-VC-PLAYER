from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

Dumper = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

Dumper.start()
run()
