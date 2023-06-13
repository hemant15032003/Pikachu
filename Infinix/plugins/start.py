from .. import bot
from telethon import events 
import asyncio 
import openai

@bot.on(events.NewMessage(incoming=True,pattern = "/start"))
async def start(event):
  await event.reply("Hello this is Infinix bot")
  
@bot.on(events.NewMessage(incoming=True,pattern = "/get"))
async def start(event):
 a=await event.reply("Hello this is get command")
 await asyncio.sleep(3)
 await a.edit("this is edit message")
  
  
@bot.on(events.NewMessage(incoming=True,pattern = "/eval"))
async def start(event):
  await event.reply("Hello this is eval command")
  
  