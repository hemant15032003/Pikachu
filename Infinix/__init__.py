from telethon import TelegramClient
import logging
import time

openai_key = "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"

api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="6022417765:AAGWGIXX2bWmqrTlezscPxGG69n0G7L2IkQ"

bot = TelegramClient("Infini", api_id, api_hash).start(bot_token = bot_token)