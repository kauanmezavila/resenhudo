import discord
import random

from discord import app_commands
from data import QUIZZES


class QuizView(discord.ui.View):

    def __init__(self, question):
        super().__init__(timeout=30)

        self.question = question
        self.answered = False

        for index, option in enumerate(question["options"]):
            button = discord.ui.Button(
                label=option,
                style=discord.ButtonStyle.primary
            )

            button.callback = self.create_callback(index)
            self.add_item(button)

    def create_callback(self, index):

        async def callback(interaction: discord.Interaction):

            if self.answered:
                await interaction.response.send_message(
                    "Essa pergunta já foi respondida!",
                    ephemeral=True
                )
                return

            self.answered = True

            if index == self.question["answer"]:
                result = "Acertou! 🎉"
            else:
                correct = self.question["options"][
                    self.question["answer"]
                ]
                result = f"Errou otário; A resposta era **{correct}**."

            for item in self.children:
                if isinstance(item, discord.ui.Button):
                    item.disabled = True

            await interaction.response.edit_message(
                content=result,
                view=self
            )

        return callback

    async def on_timeout(self):
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True


def setup_quiz(bot):

    @bot.tree.command(
        name="quiz",
        description="Responda a um quiz aleatório!"
    )
    async def quiz(interaction: discord.Interaction):

        if not QUIZZES:
            await interaction.response.send_message(
                "Não existem perguntas cadastradas!",
                ephemeral=True
            )
            return

        question = random.choice(QUIZZES)

        embed = discord.Embed(
            title="🌽 Show do grande milho",
            description=question["question"],
            color=discord.Color.blurple()
        )

        embed.set_footer(
            text=f"Categoria: {question['category']}"
        )

        await interaction.response.send_message(
            embed=embed,
            view=QuizView(question)
        )
