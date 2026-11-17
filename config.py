import discord
from discord import app_commands
from discord.ext import commands

from database import set_welcome_channel, get_guild_config


class WelcomeConfigView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=120)

        self.add_item(WelcomeChannelSelect())


class WelcomeChannelSelect(discord.ui.ChannelSelect):

    def __init__(self):
        super().__init__(
            placeholder="Selecione o canal de boas-vindas",
            channel_types=[discord.ChannelType.text],
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: discord.Interaction):

        channel = self.values[0]
        guild_id = interaction.guild_id

        if guild_id is None:
            await interaction.response.send_message(
                "Este comando só pode ser usado em um servidor.",
                ephemeral=True
            )
            return

        set_welcome_channel(
            guild_id,
            channel.id
        )

        await interaction.response.send_message(
            f"✅ Canal de boas-vindas configurado: {channel.mention}",
            ephemeral=True
        )


class Config(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="config",
        description="Configura as funcionalidades do bot"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def config(self, interaction: discord.Interaction):

        guild_id = interaction.guild_id
        if guild_id is None:
            await interaction.response.send_message(
                "Este comando só pode ser usado em um servidor.",
                ephemeral=True
            )
            return

        settings = get_guild_config(guild_id)

        channel_id = settings.get("welcome_channel_id")

        guild = interaction.guild
        channel = guild.get_channel(channel_id) if guild and channel_id else None

        embed = discord.Embed(
            title="⚙️ Configurações do servidor",
            description="Selecione abaixo o canal de boas-vindas.",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="Canal atual",
            value=channel.mention if channel else "Não configurado",
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            view=WelcomeConfigView(),
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Config(bot))
