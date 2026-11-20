<div align="center">
  <h1>Resenhudo</h1>
  <p>O bot mais resenha do Brasil no seu discord!</p>
  <p><b>v0.1.0: Membro da Resenha</b></p>
  <p>| <a href="https://github.com/kauanmezavila/resenhudo/blob/main/README-pt-br.md">🇧🇷 PT-BR</a> | <a href="https://github.com/kauanmezavila/resenhudo/blob/main/README.md">🇺🇸 EN</a> |</p>
  <img src="media/THEPCISTA.jpg">
</div>

## O que é?

Resenhudo, é o bot mestre da resenha; não importa a situação, ele estará lá pronto para fazer os membros rirem!

## Instalação

Instale no seu servidor clicando [aqui](https://discord.com/oauth2/authorize?client_id=1564434767179686079&permissions=125952&integration_type=0&scope=bot)

## Resenhas disponíveis

| Tipo    | Nome         | Ação                                                       |
| ------- | ------------ | ---------------------------------------------------------- |
| Trigger | 67           | Responde mensagens relacionadas a 67 com um gif            |
| Trigger | Resenha      | Responde mensagens relacionadas a 'resenha' com um gif     |
| Trigger | Calabreso    | Responde mensagens relacionadas a 'calabreso' com um gif   |
| Trigger | Cem reais    | Responde mensagens relacionadas a '100 reais' com um vídeo |
| Trigger | JE           | Responde mensagens relacionadas a JE com uma música        |
| Trigger | Devagar Pai  | Responde mensagens relacionadas a 'devagar' com um vídeo   |
| Trigger | Entrosa      | Responde mensagens relacionadas a 'entrosa' com uma imagem |
| Trigger | Larp         | Responde mensagens relacionadas a 'larp' com uma imagem    |
| Comando | /sofrer      | Toca uma do periclão, pode marcar alguém                   |
| Comando | /filme       | Aleatoriza um filme                                        |
| Comando | /series      | Aleatoriza uma série                                       |
| Comando | /luck        | Aleatoriza uma frase                                       |
| Comando | /roast       | Zoa alguém, pode marcar                                    |
| Comando | /enemys      | Marca quem não tem inimigos                                |
| Comando | /gado        | Avalia quão gado alguém é                                  |
| Comando | /skill-issue | Avalia se foi skill-issue                                  |
| Comando | /fofoca      | Conta uma fofoca                                           |
| Comando | /trending    | Puxa os 10 melhores repos do Github                        |
| Comando | /entrosa     | Uma arma contra os entrosas                                |
| Comando | /larp        | Larpe alguém                                               |
| Comando | /avaliar     | Avalia quão resenha algo é                                 |
| Comando | /universo    | Monte um universo absurdo                                  |
| Comando | /caraoucoroa | Jogar cara ou coroa                                        |
| Comando | /dado        | Joga um dado, pode escolher número de faces                |
| Comando | /advinhar    | Joga o jogo de advinhar que número estou pensando          |
| Comando | /daily       | Uma resenha baseada no dia                                 |
| Comando | /aura        | Avalia quanta aura alguém tem                              |
| Comando | /curriculum  | Gera o currículo do membro                                 |
| Comando | /noticia     | Faz notícias absurdas dos membros do servidor              |

## Arquitetura

O bot usa discord.py, e, o código usa uma estrutura modular:

- [bot.py](https://github.com/kauanmezavila/resenhudo/blob/main/bot.py) ações do bot
- [triggers.py](https://github.com/kauanmezavila/resenhudo/blob/main/triggers.py) triggers para ações
- [gifs.py](https://github.com/kauanmezavila/resenhudo/blob/main/gifs.py) fontes de gifs para as ações
- [data.py](https://github.com/kauanmezavila/resenhudo/blob/main/data.py) dados para as ações
- [server.py](https://github.com/kauanmezavila/resenhudo/blob/main/server.py) pra rodar no Render
- [github.py](https://github.com/kauanmezavila/resenhudo/blob/main/github.py) dados do Github para as ações
- [calcs.py](https://github.com/kauanmezavila/resenhudo/blob/main/calcs.py) cálculos para as ações

### **Como o bot fica on 24/7 no Render gratuito?**

Um guiazinho pra você amigo indie hacker sem dinheiro (igual eu):

1. Crie uma rota no seu bot /health
2. Va no [Uptimerobot](uptimerobot.com)
3. Coloque a rota /health lá pra cada 10-5 min
4. Pronto! O bot nunca dorme.
