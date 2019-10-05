# Documento de visão Glória Bot

### 1. Introdução

#### 1.1 Objetivo
Esse documento visa especificar de maneira geral as características do
desenvolvimento do ChatBot Glória (Her), deixando claro seu objetivo, razão de
sua necessidade, características, utilidade e requisitos do sistema.

#### 1.2 Escopo
O Chatbot Glória possuirá três funcionalidades
funcionalidades juntas, formam o escopo do software.
principais.
Essas
O bot terá como primeira funcionalidade indicar a localização de delegacias
próximas, onde o usuário poderá informar qualquer localidade do distrito federal e
assim obter informações á respeito das delegacias deste.
A segunda funcionalidade do Chatbot será dar explicações jurídicas. Portanto,
com base nas dúvidas ou situações apresentadas, ele ajudará com
informações jurídicas sobre assuntos relacionados a violência doméstica e
abuso.
A terceira funcionalidade é a de ensinar sobre os direitos da mulher, como o
que fazer em caso de violência, fornecer índices gráficos de violência
doméstica por localidade e auxílio para denúncias.
Por fim, Glória também será capaz de detectar as palavras usadas e cruzar
com informações da Delegacia da mulher para entender o nível de violência
que a vítima está sofrendo e pedirá um apelido no primeiro contato para
continuar a conversa em outras oportunidades. Essa funcionalidade foi inserida
no planejamento de produto, mas não de projeto. O intuito é que com o tempo,
ela deva aprender, com a ajuda de psicólogos, a ser menos fria, buscará a
empatia da interlocutora.

#### 1.3 Visão Geral
Este documento descreve de forma detalhada o embasamento, o planejamento
e a construção do ChatBot Glória. Para isso, serão apresentados tópicos
referentes a descrição do problema a ser solucionado, posicionamento do
produto em relação ao mercado, as partes interessadas e usuários, perspectiva
geral do produto: recursos e restrições, e requisitos para a aplicação do
produto.

### 2. Planejamento

#### 2.1 Oportunidade de Negócios
Um dos principais fatores que impedem a mulher em situação de violência
doméstica de denunciar o agressor é a vergonha: de ter se submetido às
agressões, de não ter tido coragem ou condição de sair do relacionamento, de
ser enxergada como vítima e, sobretudo, de ser julgada. Mas, e se o rosto da
confidente for virtual? É aí que entra Glória, um robô de inteligência artificial
pensada especificamente para estender a mão a mulheres que precisam de
ajuda.

#### 2.2 Declaração do Problema

O Problema | Afeta | Impacto | Solução
-----------|-------|---------|--------
Dificuldades e impeditivos para denúncia de abusos domésticos | Mulheres vítimas de violência e/ou abuso por seus companheiros e/ou familiares | Muitas das vítimas não denunciarem o agressor/abusador | Facilitar o acesso a informações, meios para denuncia e amparo da vítima de uma maneira mais pessoal

#### 2.3 Declaração da Posição do Produto

Para | Que | A Glória | Que | Diferente de | Nosso Produto
-----|-----|----------|-----|--------------|--------------
Mulheres vítimas de violência e/ou abuso por seus companheiros e/ou familiares | Desejam saber informações sobre como denunciar e um auxílio mais pessoal | É um chatbot | Informa sobre estastísticas de abuso, direitos das mulheres e auxília em denuncias | Atendimentos por telefone ou pessoais em delegacias, evitando o "constrangimento" relatado pelas vítimas | Fornece um atendimento pessoal e anonimamente para que vítimas se sintam mais seguras e acolhidas

### 3. Descrições da Parte Interessada e do Usuário

#### 3.1 Resumo da parte interessada

Nome | Descrição | Responsabilidade
-----|-----------|-----------------
Equipe de desenvolvimento | Graduandos em Engenharia de Software, cursando a disciplina Métodos de Desenvolvimento de Software, pela Universidade de Brasília. | Desenvolver o software no período estipulado, bem como testá-lo e implementá-lo. Gestão de equipe de desenvolvimento. Garantir a aplicação do ágil e viabilidade do projeto.
Joênio Costa | Professor da Universidade de Brasília, do curso de Engenharia de Software | Orientar, acompanhar e avaliar o projeto

#### 3.2 Resumo do Usuário

Nome | Descrição | Responsabilidade
-----|-----------|-----------------
Mulheres vítimas de violência e/ou abuso por seus companheiros e/ou familiares | Pessoas interessadas em receber dados e informações sobre direitos das mulheres e auxílio em caso de denúncias | Utilizar o ChatBot nas plataformas disponíveis

#### 3.3 Ambiente do Usuário

O Chatbot Glória poderá ser acessado através Telegram, sendo necessário um
browser ou aplicativo Telegram, conexão com a internet e uma conta na
plataforma.

#### 3.4 Necessidades Principais do Investidor ou Usuário

Necessidade | Prioridade | Interesse | Solução Atual | Solução Proposta
------------|------------|-----------|---------------|-----------------
Indicar a localização de delegacias próximas | Alta | Facilitar o acesso à informação com maior praticidade | Buscar em aplicações e ou mapas | Obter através de uma conversa com um ChatBot
Auxiliar com informações jurídicas | Alta | Facilitar o acesso à informação com maior praticidade | Buscar em sites e/ou livros, conversas com pessoas da área | Obter a informação através de uma corversa com um ChatBot

### 4. Visão Geral do Produto

#### 4.1 Perspectiva do Produto

O software será um chatbot com o qual o usuário pode conversar em
linguagem natural, podendo pedir informações jurídicas e indicações de
delegacias próximas com base no local fornecido pelo usuário.

#### 4.2 Resumo de Recursos

Benefícios para o cliente | Recursos de suporte
--------------------------|--------------------
Comunicação em linguagem natural | A troca de informações ocorre no formato de uma conversa
Fácil acesso à delegacias próximas | O Bot manda mensagens para o usuário indicando as delegacias mais próximas do local fornecido
Fácil acesso a informações jurídicas | O Bot informa ao usuário sobre direitos das mulheres e fornece dados estatísticos sobre determinador assuntos, auxiliando em caso de denúncias.

#### 4.3 Licenciamento
O ChatBot será distribuído sob a licença MIT para softwares livres, que dá
liberdade para todos que o adquirirem de modificar, distribuir, sublicenciar,
vender e contribuir para o software.

### 5. Recursos do Produto

- Plataforma de comunicação em linguagem natural.
- Permitir o usuário acesso a localização de delegacias próximas com
base na localização fornecida.
- Auxílio com explicações jurídicas ao usuário
- Fornecimento de informações como:
	- Direitos das mulheres
	- Dados estatísticos sobre violência doméstica/sexual

### 6. Restrições do Produto

#### 6.1 Restrições de Implementação
O sistema será implementado utilizando as tecnologias --- para o banco de
dados e framework Rasa, que utiliza a linguagem Python.

#### 6.2 Restrições externas
Inexperiência, curto período de tempo e a falta de um grupo de EPS podem se tornar grandes riscos para
o desenvolvimento do produto.

#### 6.3 Restrições de Design
O sistema deve ser feito em uma interface de fácil usabilidade, ou seja, uma
interface intuitiva para o usuário.

#### 6.4 Restrições de Uso
Para utilização do Glória, o usuário necessita de uma conexão com a internet e
conta no Telegram.

#### 6.5 Restrições de Confiabilidade

O sistema terá uma cobertura de testes de no mínimo 90% do sistema

### 7. Faixas de Qualidade
Toda da interação com o software deve ocorrer na forma de uma conversa
natural. Deve ser fácil entender como se usar todos os recursos do ChatBot
apenas interagindo com ele. O software oferecerá consistência e
confiabilidade, considerando que problemas na plataforma de uso escolhida
(Telegram) podem afetar o funcionamento desse serviço.

### 8. Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do
documento de visão. Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html. Acesso em: 09 setembro, 2019;
- RODRIGUES, Adrielly; BELEZA, Caio César; AGUIAR, Guilherme; ROSA, João Vitor; COELHO, Victor Hugo. Projeto Gerencia mais:Documento de Visão. Disponível em: https://github.com/fga-eps-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/Mds/Documento_de_Visao.md#3.3.2. Acesso em: 09 setembro, 2019;
- KAMAL, Byron; CERQUEIRA, Eduardo; ALVES, Gabriel; ARAGÃO, Igor;GUIMARÃES, Igor; JARDIM, João Pedro; DOS SANTOS, Marcelo;ASSUNÇÃO, Mateus; ALMEIDA, William. Projeto IncluCare: Documento de Visão. Disponível em: https://github.com/fga-eps-mds/2018.1-IncluCare_API/blob/master/docs/VISION_DOCUMENT.md.Acesso em: 09 setembro, 2019;
- FREITAS, Esio; DUTRA, Lucas; FÉO, Pedro; KADER, Saleh; FALANEH, Youssef. Projeto Kalkuli: Documento de Visão. Disponível em: https://github.com/fga-eps-mds/2018.2-Kalkuli/blob/master/docs/DocumentoDeVisao.md. Acesso em: 09 setembro, 2019;
- Open Source Initiative: The MIT License. Disponivel em: https://opensource.org/licenses/MIT. Acesso em: 09 setembro, 2019;
- ADIDA, Ben. Understanding Open-Source Licensing. Disponível em: https://openacs.org/about/licensing/open-source-licensing . Acesso em: 09 setembro 2019.
- CONTAIFER, Juliana. Conheça Glória: robô que acolherá mulheres em situação de violência. Disponível em:https://www.metropoles.com/violencia-contra-a-mulher/conheca-gloria-robo-que-acolhera-mulheres-em-situacao-de-violencia. Acesso em: 09, setembro, 2019.
- MITRA, Rudradeb. Are there Patterns in Sexual Violence? Disponível em: https://medium.com/omdena/are-there-patterns-in-sexual-violence-43b1a670a94a. Acesso em: 09, setembro, 2019.
