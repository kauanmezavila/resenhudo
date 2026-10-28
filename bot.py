import os
import random
import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

from server import webStart

from triggers import *
from gifs import *
from data import *

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
        name="O Mentalista"
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

@bot.tree.command(name="serie", description="Sorteia um episódio resenha")
async def serie(interaction: discord.Interaction):
    def sortear_episodio():
        serie, temporada, episodio, titulo, nota = random.choice(
            EPISODIOS_RESENHA
        )

        return (
            f"🎬 **{serie}**\n"
            f"📺 Temporada {temporada}, episódio {episodio}\n"
            f"🎞️ **{titulo}**\n"
            f"⭐ Nota da curadoria: {nota}/10"
        )

    await interaction.response.send_message(sortear_episodio())

@bot.tree.command(name="filme", description="Sorteia um filme ABSOLUTE CINEMA")
@app_commands.describe(categoria="Gênero do filme")
async def filme(interaction: discord.Interaction, categoria = None):
    def sortear_filme(categoria=None):
        filmes = FILMES_RESENHA

        if categoria:
            filmes = [
                filme for filme in FILMES_RESENHA
                if filme[2].casefold() == categoria.casefold()
            ]

        if not filmes:
            return "Não encontrei filmes nessa categoria."

        titulo, ano, genero, nota = random.choice(filmes)

        return (
            f"🎬 **{titulo} ({ano})**\n"
            f"🎭 Gênero: {genero}\n"
            f"⭐ Nota da curadoria: {nota}/10"
        )

    await interaction.response.send_message(sortear_filme(categoria))


if TOKEN:
    bot.run(TOKEN)
else:
    print("[DEV] Arquivo carregado, Token faltando")
