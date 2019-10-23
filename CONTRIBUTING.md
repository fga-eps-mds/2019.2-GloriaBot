# Guia de Contribuição

## O que devo saber antes de comerçar a contribuir?

Acesse o [Leia-me](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/master/README.md "README") para saber mais sobre o nosso projeto, requerimentos do sistema e como rodar a aplicação.

Leia também o nosso [Código de Conduta](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/master/CODE_OF_CONDUCT.md "Code of Conduct")

## Templates

Para fazer qualquer contribuição, deve-se seguir os seguintes templates: 

* [Feature request template](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/developer/.github/ISSUE_TEMPLATE/feature_request.md "Feature request")
* [Bug report template](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/developer/.github/ISSUE_TEMPLATE/bug_report.md "Bug report")
* [User story template](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/developer/.github/ISSUE_TEMPLATE/user-story-template.md "US")

# Como posso contribuir?

## Reportando problemas

Antes de reportar uma falha, veja se já foi reportado na lista de issue abertas, alguém já pode ter reportado isso. Algumas informações são necessárias na hora de reportar um problema:

* Seu título deve ser claro e objetivo
* Descrever como chegou a esse problema
* Comentar qual era o comportamento esperado e qual foi o comportamento apresentado
* Incluir imagens que podem ajudar na identificação do problema
* Informar qual sistema operacional você está usando
* Informar qual versão do sistema você encontrou o problema

## Sugestões de melhorias

Antes de sugerir uma melhoria, veja se já foi sugerido na lista de issues abertas, alguém já pode ter sugerido isso. Algumas informações são necessárias na hora de sugerir uma melhoria:

* Seu título deve ser claro e objetivo
* Descreva como a melhoria funcionaria passo a passo e onde isso seria inserido
* Forneça exemplos
* Incluir imagens que podem exemplificar a melhoria
* Explique por que a melhoria seria útil
* Informar qual sistema operacional você está usando
* Informar qual versão do sistema você implementou a melhoria

## Como rodar o GlóriaBot

### Primeiros passos

#### Instalando o Docker

Os links a seguir são um guia para a instalação da ferramenta Docker. Basta escolher o seu sistema operacional.

* [Docker](https://docs.docker.com/install/ "Docker")
* [Docker-compose](https://docs.docker.com/compose/install/#install-compose "Docker-compose")

#### Crie um bot no Telegram

Use o [@BotFather on Telegram](https://t.me/BotFather "BotFather") e crie um bot seguindo as instruções

#### Exportando as variáveis do bot

Depois de escolher um nome para o bot, @BotFather te dará um token que será usada para acessar a Telegram's API. Coloque ambas no arquivo credentials.yml como o exemplo a seguir. Troca o campo TELEGRAM_ACESS_TOKEN com o token que lhe foi dado pelo @Botfather e TELEGRAM_BOT_NAME com o nome do seu bot.

```
access_token: "TELEGRAM_ACESS_TOKEN"
verify: "TELEGRAM_BOT_NAME"
```

#### Instalando o ngrok

Siga as instruções na página do [ngrok](https://ngrok.com/download "Ngrok") para baixar e instalar o ngrok

#### Executando o ngrok

Conforme a seguir, execute o ngrok na porta 5005

```./ngrok http 5005```

#### Exportando a URL do Webhook e conectando ao Telegram

No terminal que está rodando o ngrok, algumas informaçoes aparacem sobre a sessão que foi iniciada. Copie a url que está no campo Forwading, é algo como:

```https://0x00000x.ngrok.io```

Pegue essa chave e troque no campo NGROK_WEBHOOK_URL na pasta credentials.yml

``` webhook_url: "NGROK_WEBHOOK_URL"```

**Observação: A url muda toda vez que ngrok é executado, sendo é necessário substituir-lo arquivo credencials.yml**

#### Baixando os arquivos

É necessário fazer o download dos arquivos para subir a aplicação:

* Dê o fork no nosso repositório [GlóriaBot](https://github.com/fga-eps-mds/2019.2-GloriaBot "GlóriaBot")

#### Docker/Docker-compose

A aplicação utilizada para gerenciar containers foi o [portainer](https://github.com/portainer/portainer "portainer"). Execute os seguintes comandos na pasta do GlóriaBot.

```$ sudo docker volume create portainer_data```

```$ sudo docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer```

#### Inicializando o Rasa

O Makefile apresenta todos os comandos reunidos e simplificados para utilização do Docker-compose. Execute os seguintes comandos na pasta do GlóriaBot.

* O comando ```train``` treina o NLU data and stories e salva o modelo treinado em ```./models```.

```$ sudo make train```

* O comando ```run``` Inicia o Rasa server com o modelo treinado.

```$ sudo make run```

Depois desse comando, é possível usar o chat.