
# Gloria Bot

## Sobre o Produto

### Introdução

Glória é um ChatBot que principal função é o auxílio de mulheres vítimas de abuso doméstico que buscam sair de sua situação de risco.

### Problema

Para mulheres vítimas de abuso doméstico existem muitas dificuldades e impeditivos para denunciar tais abusos, sejam estes impeditivos psicológicos ou físicos.

### Objetivo

O ChatBot Glória pretende ajudar mulheres em situações de abuso doméstico, facilitando acesso a informação de medidas cabíveis, meios para denúncia e amparo pessoal, a vítima pode sofrer de medo ou vergonha para realizar a denúncia presencialmente e é aí que entra Glória, que tem a finalidade de estender a mão a mulheres que precisem de ajuda.

### Principais funcionalidades

   - Indicar quais as delegacias mais próximas a vítima procurando socorro.

   - Dar explicações jurídicas a vítima, podendo assim informar sobre quais as melhores medidas a serem tomadas.

   - Informar o que fazer caso esteja sofrendo abuso doméstico, explicar quais são os direitos da vítima e usar de argumentos e dados para que seja possível encorajar a vítima a buscar ajuda.

   - Detectar uso de palavras-chave e cruzar informações para determinar o grau de abuso sofrido.

### Plataforma

O ChatBot Glória poderá ser acessado via Telegram, sendo necessário o aplicativo ou sua versão web, acesso a internet e um cadastro na plataforma.

### Contribuindo com o projeto

Para contribuir com o projeto, há um [Guia de Contribuição](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/master/CONTRIBUTING.md "Contributing") com as informações necessárias para rodar a aplicação.

#### O condigo de conduta para as contribuições está disponível [aqui](https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/master/CODE_OF_CONDUCT.md "Code of Conduct").

### Licenciamento

A Glória será distribuída sob a licença MIT para softwares livres, que dá liberdade para todos que a adquirirem de modificar, distribuir, sublicenciar, vender e contribuir para o software.

### Restrições do produto

   - O sistema será implementado utilizando as tecnologias mongoDB para o banco de dados e framework Rasa, que utiliza a linguagem Python.

   - O sistema deve ser feito em uma interface de fácil usabilidade, ou seja, uma interface intuitiva para o usuário.

   - Para utilização do Glória, o usuário necessita de uma conexão com a internet e conta no Telegram.

   - O sistema terá uma cobertura de testes de no mínimo 90% do sistema.

### Riscos

   - Inexperiência e o curto período de tempo podem se tornar grandes riscos para o desenvolvimento do produto.

   - Se adaptar aos métodos de desenvolvimento pode se provar algo difícil para alguns membros da equipe.

   - Divergência de horários da equipe pode dificultar a fluidez de desenvolvimento.

   - Problemas de equipamentos ou falta deles pode atrasar desenvolvimento do produto.

### Faixas de qualidade

Toda da interação com o software deve ocorrer na forma de uma conversa natural. Deve ser fácil entender como se usar todos os recursos do ChatBot apenas interagindo com ele. O software oferecerá consistentência e confiabilidade, considerando que problemas na plataforma de uso escolhida podem afetar o funcionamento desse serviço.

### Equipe

**Integrante** | **Github** | **Função** | **email**
---------------|------------|------------|-----------
Gabriel Hussein| @GabrielHussein | Scrum Master | gabrielhussein83@gmail.com
Rafael Ribeiro| @rafaelflarrn | Product Owner | rafaelflarrn@gmail.com
Victor Amaral | @VictorAmaralC | Developer | victorchubaka@gmail.com
Iago Theophilo | @IagoTheophilo | Developer | iagotheophilolim@gmail.com
Itallo Gravina | @itallogravina | Developer | itallo.gravina@gmail.com

A equipe é formada por graduandos em Engenharia de Software da Universidade de Brasília, cursando a disciplina Métodos de Desenvolvimento de Software. Além da equipe de desenvolvimento o Professor Joênio Costa da Universidade de Brasília agirá como orientador e avaliador do projeto.

### Como instalar e utilizar o bot
Para utilizar o Bot são necessários os seguintes requisitos:

* Docker
* Docker Compose
* Git
* Make

Copie a URL do repositório via interface do GitHub e insira no terminal

`git clone https://github.com/fga-eps-mds/2019.2-GloriaBot.git`

Após o clone em 2019.2-GloriaBot/bot insira para treinar o bot

`sudo make train`

Depois de treinar se desejado pode ser utilizada a interface do rasa via terminal para testes com o Bot

`sudo make shell`
