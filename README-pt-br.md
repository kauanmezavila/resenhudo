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

| Nome         | Ação                                                        |
| ------------ | ----------------------------------------------------------- |
| Trigger      | Responde mensagens relacionadas a certos tipos de conteúdos |
| /sofrer      | Toca uma do periclão, pode marcar alguém                    |
| /filme       | Aleatoriza um filme                                         |
| /series      | Aleatoriza uma série                                        |
| /luck        | Aleatoriza uma frase                                        |
| /roast       | Zoa alguém, pode marcar                                     |
| /enemys      | Marca quem não tem inimigos                                 |
| /gado        | Avalia quão gado alguém é                                   |
| /skill-issue | Avalia se foi skill-issue                                   |
| /fofoca      | Conta uma fofoca                                            |
| /trending    | Puxa os 10 melhores repos do Github                         |
| /entrosa     | Uma arma contra os entrosas                                 |
| /larp        | Larpe alguém                                                |
| /avaliar     | Avalia quão resenha algo é                                  |
| /universo    | Monte um universo absurdo                                   |
| /caraoucoroa | Jogar cara ou coroa                                         |
| /dado        | Joga um dado, pode escolher número de faces                 |
| /advinhar    | Joga o jogo de advinhar que número estou pensando           |
| /daily       | Uma resenha baseada no dia                                  |
| /aura        | Avalia quanta aura alguém tem                               |
| /curriculum  | Gera o currículo do membro                                  |
| /noticia     | Faz notícias absurdas dos membros do servidor               |
| /advogado    | _"Better Call Resenhudo!"_                                  |
| /quiz        | Um quiz simples                                             |
| /8ball       | A clássica bola oito                                        |
| /canon       | Veja se algo é canon ou filler                              |
| /vocêprefere | Um simples jogo de você prefere                             |
| /kind        | Uma frase gentil                                            |

## Arquitetura

O bot usa discord.py, e, o código usa uma estrutura modular:

- [bot.py](https://github.com/kauanmezavila/resenhudo/blob/main/bot.py) ações do bot
- [triggers.py](https://github.com/kauanmezavila/resenhudo/blob/main/triggers.py) triggers para ações
- [gifs.py](https://github.com/kauanmezavila/resenhudo/blob/main/gifs.py) fontes de gifs para as ações
- [data.py](https://github.com/kauanmezavila/resenhudo/blob/main/data.py) dados para as ações
- [server.py](https://github.com/kauanmezavila/resenhudo/blob/main/server.py) pra rodar no Render
- [github.py](https://github.com/kauanmezavila/resenhudo/blob/main/github.py) dados do Github para as ações
- [calcs.py](https://github.com/kauanmezavila/resenhudo/blob/main/calcs.py) cálculos para as ações
- [quiz.py](https://github.com/kauanmezavila/resenhudo/blob/main/quiz.py) a ação de quiz

### **Como o bot fica on 24/7 no Render gratuito?**

Um guiazinho pra você amigo indie hacker sem dinheiro (igual eu):

1. Crie uma rota no seu bot /health
2. Va no [Uptimerobot](uptimerobot.com)
3. Coloque a rota /health lá pra cada 10-5 min
4. Pronto! O bot nunca dorme.
