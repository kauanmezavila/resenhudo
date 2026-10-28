<div align="center">
  <h1>Resenhudo</h1>
  <p>O bot mais resenha do Brasil no seu discord!</p>
  <p><b>v0.0.1: Aprendiz da resenha</b></p>
</div>

## O que é?

Resenhudo, é o bot mestre da resenha; não importa a situação, ele estará lá pronto para fazer os membros rirem!

## Instalação

Instale no seu servidor clicando [aqui](https://discord.com/oauth2/authorize?client_id=1564434767179686079&permissions=68608&integration_type=0&scope=bot+applications.commands)

## Resenhas disponíveis

- 67 trigger: algum membro disse "67"? O resenhudo está aguardando com um gif na mão...
- Resenha trigger: citaram resenha? O resenhudo vai averiguar!

## Arquitetura

O bot utiliza o framework discord.py, além disso, o código utiliza de uma infraestrutura modular, aonde ações do bot estão em [bot.py](https://github.com/kauanmezavila/resenhudo/blob/main/bot.py), os triggers para ações em [triggers.py](https://github.com/kauanmezavila/resenhudo/blob/main/triggers.py), e os gifs em [gifs.py](https://github.com/kauanmezavila/resenhudo/blob/main/gifs.py)

**Como o bot fica on 24/7 no Render gratuito?**
Um guiazinho pra você amigo indie hacker sem dinheiro (igual eu):

1. Crie uma rota no seu bot /health
2. Va no [Uptimerobot](uptimerobot.com)
3. Coloque a rota /health lá pra cada 10-5 min
4. Pronto! O bot nunca dorme.
