import os
import random
import discord
from dotenv import load_dotenv

from discord.ext import commands
from server import webStart

load_dotenv()

TOKEN = os.getenv("TOKEN")
webStart()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


GIFS_67 = [
    "https://c.tenor.com/U94DkrDstecAAAAd/tenor.gif",
    "https://c.tenor.com/I72UDkaxRyIAAAAC/tenor.gif",
    "https://c.tenor.com/Lnt2uEm1vrUAAAAd/tenor.gif",
]

GIFS_RESENHA = [
    "https://c.tenor.com/D2cIrVCGgdwAAAAC/tenor.gif",
]

SIX_SEVEN_TRIGGERS = [
    "67",
    "six seven",
    "six-seven",
    "sixseven",
    "six  seven",
    "six/seven",
    "six_seven",
    "six seven!",
    "six seven!!",
    "meia sete",
    "meia-sete",
    "seis sete",
    "seis-sete",
    "seis e sete",
    "sessenta e sete",
    "67 meme",
    "67 moment",
    "67 moments",
    "67 kid",
    "67 brainrot",
    "67 reference",
    "67 never dies",
    "67 forever",
    "67 is life",
    "67 is everywhere",
    "67 mentioned",
    "67 spotted",
    "67 detected",
    "67 🗣️",
    "67 🔥",
    "67 💀",
    "67 🫱🫲",
    "6 7",
    "6-7",
    "6_7",
    "6/7",
    "6.7",
    "6,7",
    "6️⃣7️⃣",
    "67",
    "٦٧",
    "六七",
    "what the 67",
    "only in 67",
    "bro said 67",
    "someone said 67",
    "who said 67",
    "never skip 67",
    "67 strikes again",
    "here comes 67",
    "the 67 is real",
    "it's 67",
    "its 67",
    "we got 67",
    "67 before gta 6",
    "67 in chat",
    "67 mentioned in chat",
]

RESENHA_TRIGGERS = [
    "averiguar resenha",
    "Averiguar resenha",
    "averigue a resenha",
    "resenha",
    "Resenha",
    "resenha?",
    "Resenha?",
]


@bot.event
async def on_ready():
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


if TOKEN:
    bot.run(TOKEN)
else:
    print("[DEV] Arquivo carregado, Token faltando")
