import os
import random
import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

from server import webStart

from triggers import *
from gifs import *

class Bot(commands.Bot):
    async def setup_hook(self):
        await self.tree.sync()

load_dotenv()

TOKEN = os.getenv("TOKEN")
webStart()

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="A resenha já ta on?"
    )

    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )

    print(f"{bot.user} ACORDOU")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    texto = message.content.lower()

    if any(trigger in texto for trigger in SIX_SEVEN_TRIGGERS):
        if random.random() < 0.85:
            gif = random.choice(GIFS_67)
            await message.reply(gif)

    if any(trigger in texto for trigger in RESENHA_TRIGGERS):
        if random.random() < 0.85:
            gif = random.choice(GIFS_RESENHA)
            await message.reply(gif)

    await bot.process_commands(message)

@bot.tree.command(
    name="ping",
    description="Verifica a latência do bot"
)
async def ping(interaction: discord.Interaction):
    ms = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! Latência: {ms} ms",
        ephemeral=True
    )


if TOKEN:
    bot.run(TOKEN)
else:
    print("[DEV] Arquivo carregado, Token faltando")
