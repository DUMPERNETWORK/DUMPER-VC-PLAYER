from pyrogram import Client as Dumper

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

dumper = Dumper(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

dumper.start()
run()
