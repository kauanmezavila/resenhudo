<div align="center">
  <h1>Resenhudo</h1>
  <p>The most resenha bot on your server!</p>
  <p><b>v0.1.0: Member of Resenha</b></p>
  <p>| <a href="https://github.com/kauanmezavila/resenhudo/blob/main/README-pt-br.md">🇧🇷 PT-BR</a> | <a href="https://github.com/kauanmezavila/resenhudo/blob/main/README.md">🇺🇸 EN</a> |</p>
  <img src="media/THEPCISTA.jpg">
</div>

## What it is?

Resenhudo, is the master of the resenha; don't mather the situation, he will be there to make everyone laughs!

> Hey! This bot is made thinking about the Brazilian Public.
> Every type of humour and things here are completely normal
> and comic for the destinated public

## Installation

Install in your server clicking [here](https://discord.com/oauth2/authorize?client_id=1564434767179686079&permissions=125952&integration_type=0&scope=bot)

## Avaliable resenhas

| Tipo    | Nome         | Ação                                                |
| ------- | ------------ | --------------------------------------------------- |
| Trigger | 67           | Answer messages related to 67 with a gif            |
| Trigger | Resenha      | Answer messages related to 'resenha' with a gif     |
| Trigger | Calabreso    | Answer messages related to 'calabreso' with a gif   |
| Trigger | Cem reais    | Answer messages related to '100 reais' with a video |
| Trigger | JE           | Answer messages related to JE with a music          |
| Trigger | Devagar Pai  | Answer messages related to 'devagar' with a video   |
| Trigger | Entrosa      | Answer messages related to 'entrosa' with a image   |
| Trigger | Larp         | Answer messages related to 'larp' with a image      |
| Command | /sofrer      | Play on music from Péricles, can mark someone       |
| Command | /filme       | Randomize a film                                    |
| Command | /series      | Randomize a serie                                   |
| Command | /luck        | Randomize a phrase                                  |
| Command | /roast       | Roast someone, can mark someone                     |
| Command | /enemys      | Mark someone that doens't have enemies              |
| Command | /gado        | Judges how much someone is simp                     |
| Command | /skill-issue | Judges if something was a skill-issue               |
| Command | /fofoca      | Tells an absurd gossip                              |
| Command | /trending    | Show the top 10 repos from Github                   |
| Command | /entrosa     | A weapon agains't the entrosas                      |
| Command | /larp        | Larp someone                                        |
| Command | /avaliar     | Judges how much something is                        |
| Command | /universo    | Build a absurd universe                             |

## Architecture

The bot uses discord.py, and, the code uses a modular architecture:

- [bot.py](https://github.com/kauanmezavila/resenhudo/blob/main/bot.py) bot actions
- [triggers.py](https://github.com/kauanmezavila/resenhudo/blob/main/triggers.py) triggers for actions
- [gifs.py](https://github.com/kauanmezavila/resenhudo/blob/main/gifs.py) gifs sources for actions
- [data.py](https://github.com/kauanmezavila/resenhudo/blob/main/data.py) data for actions
- [server.py](https://github.com/kauanmezavila/resenhudo/blob/main/server.py) to run on Render
- [github.py](https://github.com/kauanmezavila/resenhudo/blob/main/github.py) Github data for actions
- [calcs.py](https://github.com/kauanmezavila/resenhudo/blob/main/calcs.py) calculations for actions

### **How the bot can stay 24/7 on free tier Render?**

A little knowledge for you broked friend indie hacker (like me):

1. Code a /health route
2. Go on [Uptimerobot](uptimerobot.com)
3. Configure to consult the /health route every 10-5 min
4. Ready! The bot never sleeps.
