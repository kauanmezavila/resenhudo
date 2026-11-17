import os
import random
import logging
import requests
from pathlib import Path

import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands, tasks
import itertools

from server import webStart
from triggers import *
from gifs import *
from data import *
from github import *


load_dotenv()

TOKEN = os.getenv("TOKEN")

BASE_DIR = Path(__file__).resolve().parent
CEMPILA_VIDEO_PATH = BASE_DIR / "media" / "100Reais????.mp4"
SOFRER_MUSIC = BASE_DIR / "media" / "ate-que-durou.mp3"
JE_MUSIC = BASE_DIR / "media" / "je.wav"
DEVAGAR_VIDEO = BASE_DIR / "media" / "CalmaPaizin.mp4"
TORFIN_MUSIC = BASE_DIR / "media" / "Aruarian Dance - Nujabes Piano Cover + Sheet Music.mp3"

LISTONA = SIX_SEVEN_TRIGGERS + RESENHA_TRIGGERS + CEMPILA_TRIGGERS + DEVAGAR_TRIGGERS + JE_TRIGGERS

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger("resenhudo")



class Bot(commands.Bot):
    async def setup_hook(self):
        await self.tree.sync()
        logger.info("Slash commands sincronizados")


intents = discord.Intents.default()
intents.message_content = True

bot = Bot(
    command_prefix="!",
    intents=intents,
)

statuses = itertools.cycle([
    discord.Activity(
        type=discord.ActivityType.watching,
        name=random.choice(LISTONA)
    ),
])


@tasks.loop(seconds=15)
async def rotate_status():
    await bot.change_presence(activity=next(statuses))

@bot.event
async def on_ready():
    if not rotate_status.is_running():
        rotate_status.start()


    logger.info("%s ACORDOU", bot.user)

@bot.event
async def on_member_join(member):
    channel = member.guild.text_channels[0]

    embed = discord.Embed(
        title="NOVO RESENHA!",
        description=f"{member.mention} chegou para a batalha RESENHAS x ENTROSAS",
        color=discord.Color.blurple()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.set_footer(
        text=f"Agora somos {member.guild.member_count} resenhas!"
    )

    await channel.send(embed=embed)


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    texto = message.content.lower()

    try:
        if any(
            trigger.lower() in texto
            for trigger in SIX_SEVEN_TRIGGERS
        ):
            if random.random() < 0.85 and GIFS_67:
                await message.reply(random.choice(GIFS_67))

        elif any(
            trigger.lower() in texto
            for trigger in RESENHA_TRIGGERS
        ):
            if random.random() < 0.85 and GIFS_RESENHA:
                await message.reply(random.choice(GIFS_RESENHA))

        elif any(
            trigger.lower() in texto
            for trigger in ENTROSA_TRIGGERS
        ):
            if random.random() < 0.85 and ENTROSAS_IMAGES:
                await message.reply(random.choice(ENTROSAS_IMAGES))

        elif any(
            trigger.lower() in texto
            for trigger in LARP_TRIGGERS
        ):
            if random.random() < 0.85 and LARP_IMAGES:
                await message.reply(random.choice(LARP_IMAGES))

        elif any(
            trigger.lower() in texto
            for trigger in CEMPILA_TRIGGERS
        ):
            if random.random() < 0.85:
                if CEMPILA_VIDEO_PATH.is_file():
                    await message.reply(
                        file=discord.File(
                            str(CEMPILA_VIDEO_PATH)
                        )
                    )
                else:
                    logger.error(
                        "Vídeo não encontrado: %s",
                        CEMPILA_VIDEO_PATH,
                    )

        elif any(
            trigger.lower() in texto
            for trigger in JE_TRIGGERS
        ):
            if random.random() < 0.85:
                if JE_MUSIC.is_file():
                    await message.reply(
                        file=discord.File(
                            str(JE_MUSIC)
                        )
                    )
                else:
                    logger.error(
                        "Áudio não encontrado: %s",
                        JE_MUSIC,
                    )

        
        elif any(
            trigger.lower() in texto
            for trigger in DEVAGAR_TRIGGERS
        ):
            if random.random() < 0.85:
                if DEVAGAR_VIDEO.is_file():
                    await message.reply(
                        file=discord.File(
                            str(DEVAGAR_VIDEO)
                        )
                    )
                else:
                    logger.error(
                        "Vídeo não encontrado: %s",
                        DEVAGAR_VIDEO,
                    )
            

    except discord.HTTPException:
        logger.exception(
            "Calma rapaziada, deu red aqui."
        )

    finally:
        await bot.process_commands(message)

@bot.tree.command(
    name="ping",
    description="Verifica a latência do bot",
)
async def ping(interaction: discord.Interaction):
    ms = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! Latência: {ms} ms",
        ephemeral=True,
    )

@bot.tree.command(
    name="luck",
    description="Frase aleatória",
)
async def luck(interaction: discord.Interaction):
    def fortune():
        url = "https://dumbapis.com/fortune"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            return data["fortune"]

        except requests.RequestException as e:
            return f"Erro ao consultar a API: {e}"
        except (ValueError, KeyError):
            return "Erro: resposta inválida da API."

    texto = f"""**Uma frase, para VOCÊ**
> {fortune()}
"""
    
    await interaction.response.send_message(
        texto,
        ephemeral=True,
    )

@bot.tree.command(
    name="info",
    description="Infos do bot",
)
async def info(interaction: discord.Interaction):

    last = get_last_commit("kauanmezavila", "resenhudo")

    texto = f"""**Resenhudo**
O Bot mais RESENHA do Brasil

- Maintainer: [ByKurebo](https://github.com/kauanmezavila)

- Sou [OPEN SOURCE!](https://kmlresearchlabs.vercel.app/resenhudo)

- Commit atual (**{last['author']}**):
> **{last['date']}**
> **{last['message']}**

- Infos nerds:
> {last['sha']}
> [URL DO COMMIT]({last['url']})

Powered by KML Research Labs
    """

    await interaction.response.send_message(
        texto,
        ephemeral=True,
        suppress_embeds=True,
    )

@bot.tree.command(
    name="trending",
    description="Veja repos no Github TENDÊNCIAS",
)
async def trending(interaction: discord.Interaction):
    resposta = get_trending()

    await interaction.response.send_message(resposta, suppress_embeds=True)

@bot.tree.command(
    name="serie",
    description="Sorteia um episódio resenha",
)
async def serie(interaction: discord.Interaction):
    if not EPISODIOS_RESENHA:
        await interaction.response.send_message(
            "Não há episódios cadastrados.",
            ephemeral=True,
        )
        return

    serie_nome, temporada, episodio, titulo, nota = (
        random.choice(EPISODIOS_RESENHA)
    )

    resposta = (
        f"🎬 **{serie_nome}**\n"
        f"📺 Temporada {temporada}, episódio {episodio}\n"
        f"🎞️ **{titulo}**\n"
        f"⭐ Nota da curadoria: {nota}/10"
    )

    await interaction.response.send_message(resposta)


@bot.tree.command(
    name="sofrer",
    description="Sofra por amor escutando o Periclão",
)
@app_commands.describe(
    user="Quem tá na sofrência por amor",
)
async def sofrer(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    if not SOFRER_MUSIC.is_file():
        logger.error(
            "Música não encontrada: %s",
            SOFRER_MUSIC,
        )

        await interaction.response.send_message(
            "❌ A música não foi encontrada.",
            ephemeral=True,
        )
        return

    alvo = user or interaction.user

    resposta = (
        f"💔 {alvo.mention}, o bar te espera :fist::pensive::tumbler_glass:\n"
        "🎶 **Até Que Durou — Periclão**"
    )

    try:
        await interaction.response.send_message(
            content=resposta,
            file=discord.File(
                str(SOFRER_MUSIC),
                filename="ate-que-durou.mp3",
            ),
        )
    except discord.HTTPException:
        logger.exception(
            "Erro ao enviar a música no comando /sofrer."
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui enviar a música. "
                "Verifique o tamanho do arquivo e os limites do Discord.",
                ephemeral=True,
            )

@bot.tree.command(
    name="enemys",
    description="Você não tem inimigos Thorfinn",
)
@app_commands.describe(
    user="Quem não tem inimigos",
)
async def enemys(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    if not TORFIN_MUSIC.is_file():
        logger.error(
            "Música não encontrada: %s",
            TORFIN_MUSIC,
        )

        await interaction.response.send_message(
            "❌ A música não foi encontrada.",
            ephemeral=True,
        )
        return

    alvo = user or interaction.user

    resposta = (
        f"{alvo.mention}, você não tem inimigos...\n"
        "🎶 **Aruarian Dance — Nujabes**"
    )

    try:
        await interaction.response.send_message(
            content=resposta,
            file=discord.File(
                str(TORFIN_MUSIC),
                filename="Aruarian Dance - Nujabes Piano Cover + Sheet Music.mp3",
            ),
        )
    except discord.HTTPException:
        logger.exception(
            "Erro ao enviar a música no comando /enemys."
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui enviar a música. "
                "Verifique o tamanho do arquivo e os limites do Discord.",
                ephemeral=True,
            )

@bot.tree.command(
    name="roast",
    description="Aquela zoada básica",
)
@app_commands.describe(
    user="Quem vai ser zoado",
)
async def roast(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    alvo = user or interaction.user

    resposta = (alvo.mention + " " + random.choice(ZUADAS))

    try:
        await interaction.response.send_message(
            content=resposta,
        )
    except discord.HTTPException:
        logger.exception(
            "Erro ao tentar zuar ele"
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui zuar ele"
                "O HTTP zuo no bagulho",
                ephemeral=True,
            )

@bot.tree.command(
    name="entrosa",
    description="Larpa esse entrosa!",
)
@app_commands.describe(
    user="Entrosa a ser LARPADO",
)
async def entrosa(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    alvo = user or interaction.user

    try:
        await interaction.response.send_message(
            content=random.choice(ENTROSAS_IMAGES))
    except discord.HTTPException:
        logger.exception(
            "Erro ao tentar larpar o entrosa."
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui larpar ele "
                "O pq eu n sei...",
                ephemeral=True,
            )

@bot.tree.command(
    name="larp",
    description="Algo sobre larp",
)
@app_commands.describe(
    user="Marca algm",
)
async def larp(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    alvo = user or interaction.user

    try:
        await interaction.response.send_message(
            content=random.choice(LARP_IMAGES))
    except discord.HTTPException:
        logger.exception(
            "Erro ao tentar larpar"
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui larpar"
                "O pq eu n sei...",
                ephemeral=True,
            )

@bot.tree.command(
    name="gado",
    description="O quão GADO você é???",
)
@app_commands.describe(
    user="Quem vai ser avaliado",
)
async def gado(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    alvo = user or interaction.user

    avaliação = "..."

    resultado = str(random.random()).replace("0.", "")[:2]

    resultadoNum = int(resultado)

    if resultadoNum == 100:
        avaliação = "GADO PURÍSSIMO; vo fala nada, tenho é dó"

    elif resultadoNum >= 80 and resultadoNum < 100:
        avaliação = "GADO; igual orelha de boi: perto do chifre e longe do rabo"

    elif resultadoNum >= 70 and resultadoNum < 79:
        avaliação = "GADINHO; já ta começando a usar coleira..."

    elif resultadoNum >= 60 and resultadoNum < 69:
        avaliação = "ASPIRANTE BOVINO; já pede foto em troca de Nitro, vergonhoso..."

    elif resultadoNum >= 50 and resultadoNum < 59:
        avaliação = "CACHORRINHO; da tempo de voltar irm"

    elif resultadoNum >= 40 and resultadoNum < 49:
        avaliação = "BRINQUEDO; damn, tu chama ela/ele de 'momoreco' e faz voz de bebê??"

    elif resultadoNum < 39:
        avaliação = "PADRÃO; dentro do limite aceitável..."

    resposta = f"**{resultado}%** {avaliação}\n> {alvo.mention}"

    try:
        await interaction.response.send_message(
            content=resposta,
        )
    except discord.HTTPException:
        logger.exception(
            "Erro ao avaliar ele"
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui avaliar ele"
                "O HTTP zuo no bagulho",
                ephemeral=True,
            )

@bot.tree.command(
    name="skill-issue",
    description="Isso foi uma Skill Issue?",
)
@app_commands.describe(
    user="Quem vai ser avaliado",
)
async def skill_issue(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    alvo = user or interaction.user

    avaliação = "..."

    resultado = str(random.random()).replace("0.", "")[:2]

    resultadoNum = int(resultado)

    if resultadoNum == 100:
        avaliação = "PRA KCT :white_check_mark::white_check_mark:"

    elif resultadoNum > 50:
        avaliação = "SKILL-ISSUE PURA :white_check_mark:"

    elif resultadoNum <= 50:
        avaliação = "NÃO :x::x:"


    resposta = f"{avaliação}\n> {alvo.mention}"

    try:
        await interaction.response.send_message(
            content=resposta,
        )
    except discord.HTTPException:
        logger.exception(
            "Erro ao avaliar ele"
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui avaliar ele"
                "O HTTP zuo no bagulho",
                ephemeral=True,
            )

@bot.tree.command(
    name="fofoca",
    description="Conte uma fofoca",
)
async def fofoca(
    interaction: discord.Interaction,
    user: discord.Member | None = None,
):
    avaliação = "..."

    pessoa1 = random.choice(FOFOCA_NOME)

    pessoa2 = random.choice(FOFOCA_NOME)
    while pessoa2 == pessoa1:
        pessoa2 = random.choice(FOFOCA_NOME)

    ação = random.choice(FOFOCA_AÇÃO)

    hora = random.choice(FOFOCA_HORA)

    resposta = f"EXTRA, EXTRA!:\n **{pessoa1} {ação} {pessoa2} {hora}**"

    try:
        await interaction.response.send_message(
            content=resposta,
        )
    except discord.HTTPException:
        logger.exception(
            "Erro ao contar uma fofoca"
        )

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ Não consegui contar uma fofoca"
                "O HTTP zuo no bagulho",
                ephemeral=True,
            )

@bot.tree.command(
    name="filme",
    description="Sorteia um filme ABSOLUTE CINEMA",
)
@app_commands.describe(
    categoria="Gênero do filme (opcional)",
)
async def filme(
    interaction: discord.Interaction,
    categoria: str | None = None,
):
    filmes = FILMES_RESENHA

    if categoria:
        categoria_normalizada = categoria.strip().casefold()

        filmes = [
            item
            for item in FILMES_RESENHA
            if item[2].casefold() == categoria_normalizada
        ]

    if not filmes:
        await interaction.response.send_message(
            "🎬 Não encontrei filmes nessa categoria.",
            ephemeral=True,
        )
        return

    titulo, ano, genero, nota = random.choice(filmes)

    resposta = (
        f"🎬 **{titulo} ({ano})**\n"
        f"🎭 Gênero: {genero}\n"
        f"⭐ Nota da curadoria: {nota}/10"
    )

    await interaction.response.send_message(resposta)



if __name__ == "__main__":
    if TOKEN:
        webStart()
        bot.run(TOKEN)
    else:
        logger.warning(
            "[DEV] Arquivo carregado, token ausente."
        )