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

| Nome         | Ação                                            |
| ------------ | ----------------------------------------------- |
| Trigger      | Answer messsages with certain types of contents |
| /sofrer      | Play on music from Péricles, can mark someone   |
| /filme       | Randomize a film                                |
| /series      | Randomize a serie                               |
| /luck        | Randomize a phrase                              |
| /roast       | Roast someone, can mark someone                 |
| /enemys      | Mark someone that doens't have enemies          |
| /gado        | Judges how much someone is simp                 |
| /skill-issue | Judges if something was a skill-issue           |
| /fofoca      | Tells an absurd gossip                          |
| /trending    | Show the top 10 repos from Github               |
| /entrosa     | A weapon agains't the entrosas                  |
| /larp        | Larp someone                                    |
| /avaliar     | Judges how much something is                    |
| /universo    | Build a absurd universe                         |
| /caraoucoroa | Play head or tails                              |
| /dado        | Play a dice, can choss number of faces          |
| /advinhar    | Play the "Guess the number i am thinking"       |
| /daily       | A resenha based on the day                      |
| /aura        | Judges hou much aura someone have               |
| /patch       | Generates a Patch Notes of someone              |
| /noticia     | Makes absurd news about the server members      |
| /advogado    | _"Better Call Resenhudo!"_                      |
| /quiz        | A simple quiz                                   |
| /8ball       | The classic 8 ball oracle                       |
| /canon       | Judges if something is canon or filler          |
| /vocêprefere | A simple would you rather game                  |
| /kind        | A really kind phrase                            |
| /alibi       | Get an alibi                                    |
| /sola        | See if someone can beat Saitama                 |
| /days        | How much days till the year end                 |

## Architecture

The bot uses discord.py, and, the code uses a modular architecture:

- [bot.py](https://github.com/kauanmezavila/resenhudo/blob/main/bot.py) bot actions
- [triggers.py](https://github.com/kauanmezavila/resenhudo/blob/main/triggers.py) triggers for actions
- [gifs.py](https://github.com/kauanmezavila/resenhudo/blob/main/gifs.py) gifs sources for actions
- [data.py](https://github.com/kauanmezavila/resenhudo/blob/main/data.py) data for actions
- [server.py](https://github.com/kauanmezavila/resenhudo/blob/main/server.py) to run on Render
- [github.py](https://github.com/kauanmezavila/resenhudo/blob/main/github.py) Github data for actions
- [calcs.py](https://github.com/kauanmezavila/resenhudo/blob/main/calcs.py) calculations for actions
- [quiz.py](https://github.com/kauanmezavila/resenhudo/blob/main/quiz.py) quiz action

## How to host

### Self host

After cloning the repo, just run

```bash
python bot.py
```

### Bot-Hosting (yes, pretty SaaS startup)

1. Go to [Bot-Hosting](https://bot-hosting.net/)
2. Follow the steps to create a application
3. On the Github confs page, simple set the repo `kauanmezavila/resenhudo`
4. Don't forget to set on initialization confs the file `bot.py`
5. Run it, don't forget to update the pushs AND don't forget to renew the Free tier plan

### **How the bot can stay 24/7 on free tier Render?**

A little knowledge for you broked friend indie hacker (like me):

1. Code a /health route
2. Go on [Uptimerobot](uptimerobot.com)
3. Configure to consult the /health route every 10-5 min
4. Ready! The bot never sleeps.
