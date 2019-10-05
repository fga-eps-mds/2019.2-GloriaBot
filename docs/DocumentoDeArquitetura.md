# Introdução
## Finalidade
  Este documento tem como finalidade fornecer uma visão geral da arquitetura do Projeto Glória, utilizando-se de diversas visões arquiteturais - tais como a visão lógica e de caso de uso - a fim de facilitar o entendimento dos processos e funcionamento de todo o sistema. Tem também como objetivo transmitir as decisões arquiteturais significativas tomadas em relação ao mesmo.
## Escopo
  Através desse documento, é possível obter um melhor entendimento da arquitetura do Projeto Glória, permitindo ao leitor compreender o funcionamento de seu sistema, como também a abordagem utilizada para o seu desenvolvimento.
# Representação Arquitetural
O estilo arquitetural de microsserviços é uma abordagem que visa implementar uma aplicação como uma suíte de pequenos serviços. Onde cada um executa um processo próprio e se comunica, geralmente, com requests HTTP. Tendo em vista a principal característica desse estilo arquitetural, a independência entre os serviços, o chatbot Glória terá microsserviços como parte de sua arquitetura.
Os serviços internos que fazem parte da Glória são:
  * API Gateway;
  * (a implementar)
  Para a execução completa do projeto será necessário o consumo de dados de fontes externas, sendo elas:
  * API Telegram;
  * (a implementar)
   Além do comportamento interno da Glória, outro fator importante a ser considerado é a criação do chatbot em si. Para isso, vários fatores precisam ser considerados, como o uso de linguagem natural. Por isso, será utilizado a tecnologia Rasa, que se divide em Rasa Core e Rasa NLU. Rasa Core é de extrema importância para criar um bot baseado em Machine Learning. Já o Rasa NLU é responsável pelo processamento da linguagem natural. Essa combinação vai garantir que a Glória tenha uma comunicação acessível com o usuário.
## Representação dos Microsserviços
### API Gateway
  Dentro de uma arquitetura de microsserviços ter um API Gateway é importante para gerenciar o acesso às API’s de um determinado sistema. Ou seja, ele é um padrão de software que funciona de forma similar a uma fachada sendo o único ponto de acesso, - que controla as entradas e saídas de dados, o tráfego de tarefas e monitora, - para as API’s internas. Sua existência reduz problemas causados pela interação entre cliente e microsserviços, além de conservar o ambiente dos serviços.
### (a implementar)

## Padrões
### Padrão API Gateway
  Uma API Gateway é um serviço responsável por uma única entrada para os serviços internos. Ela organiza e recebe as requisições externas e as distribui para os microsserviços internos. Além disso, ela precisa se preocupar com as prioridades de requisição e com autenticação.
  O Padrão API Gateway é bastante similar ao padrão Facade (Fachada), já que também encapsula a arquitetura interna e provê uma API para os usuários. Suas principais responsabilidades são encaminhar as requisições, compor a API, gerenciar os requests utilizando o padrão API Composition, - ao chamar os diferentes microsserviços e agregar os resultados em uma resposta para o usuário. Cada uma dessas responsabilidades possui características próprias e para o entendimento do padrão API Gateway é preciso entender cada uma delas.
  O encaminhamento das requisições é uma das funções principais de uma API Gateway. Ela funciona implementando operações que encaminhem as requisições para o microsserviço correto.
  A composição da API garante que a API Gateway seja mais do que um conjunto de funções para encaminhar requisições. Essa composição é feita, geralmente, utilizando o padrão API Composition.
  Além dessas duas principais responsabilidades a API Gateway lida com funções como autenticação, autorização, respostas de cache, cors e requisições de log.
### Padrão API Composition
  Ao encaminhar as requisições para os microsserviços internos a API Gateway irá desmembrar a requisição em pedidos menores e irá mandá-los para cada um dos microsserviços correspondentes. A papel do padrão API Composition é pegar os resultados individuais de cada microsserviço anteriormente solicitado e compor uma resposta única que será mandado para o usuário.
## Tecnologias
### API do Bot de Telegram
  A API de bot do Telegram permite que bots interajam diretamente com usuários por meio de mensagens e comandos. Ela será usada para um dos deploys, de forma a garantir que a Glória consiga atingir uma faixa de usuários que não utilizam o Facebook. Para isso a Glória precisará atender alguns critérios, já que o Telegram exige uma conexão HTTPS para interagir com a API e pede que todos os desenvolvedores suportem os comandos ‘/start’, ‘/help’, e ‘/settings’ em seus bots para facilitar a interação de usuários.
### Rasa

#### Fluxo básico da tecnologia Rasa
  Rasa é um conjunto de ferramentas para Python para a criação de bots. Ele tem duas principais frentes, o Rasa Core e o Rasa NLU. O Rasa Core baseia a o desenvolvimento em Machine Learning, onde você consegue treinar e atualizar as models “conversando” e provendo feedback para o bot. Já o Rasa NLU é responsável pelo processamento da linguagem natural.
# Metas e Restrições de Arquitetura
## Restrições Tecnológicas
  Para o desenvolvimenta da Glória serão utilizados as seguintes tecnologias:
  * Rasa: Conjuntos de ferramentas de Machine Learning para a criação de chatbots.
  * Python: Linguagem base utilizada no Rasa.
  * (a implementar)
## Requisitos Não Funcionais
  * O sistema deve ter integração com o Telegram;
  * O sistema deve conversar com o usuário em linguagem natural;
  * O sistema deve respeitar a personalidade do bot;
  * O sistema deve aprender novos comportamentos de acordo com a resposta do usuário;
