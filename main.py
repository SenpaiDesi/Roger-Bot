from pydoc import importfile
import discord
from discord.ext import commands , tasks
import asyncio
import datetime
import aiosqlite
from tqdm import *
import Assets
import utils

intents = discord.Intents.default()
intents.members = True
intents.messages = True


bot = commands.Bot(command_prefix=";", intents = intents, case_insensitive = True)
bot.remove_command("help")



@bot.event
async def on_ready():
    with tqdm (Assets.initial_extension, unit="Ext", desc="Loading extensions"):
        for extension in Assets.initial_extension:
            bot.load_extension(extension)
    print("Bot online\n")
        




raw_info = utils.get_json(Assets.config)
token = raw_info["token"]
bot.run(token)
