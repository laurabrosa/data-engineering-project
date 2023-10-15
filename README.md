# Data Engineering Project - Grupo 1

## Objetivo do Projeto

Complementar o conhecimento técnico adquirido na disciplina, aplicando-o em um projeto de engenharia de dados focado na análise do Bitcoin. Aqui estão os principais pontos que vamos abordar:

**Ingestão de Dados**

A primeira etapa será a ingestão de dados. Isso significa que deve ser criado uma aplicação que irá coletar informações do Coincap (uma fonte de dados sobre criptomoedas). Esses dados serão transformados e, em seguida, carregados em um banco de dados para posterior análise.

**Análise de Dados**

A segunda parte do projeto é dedicada à análise de dados. Nela, deve-se desenvolver um script que ficará atento ao valor do Bitcoin. Se o valor cair abaixo de R$130.000,00, o script enviará um e-mail de alerta. Isso nos ajudará a monitorar as flutuações do Bitcoin e tomar ações quando necessário.

📑 **Condições**

Grupo com até 4 pessoas.
Data da entrega: último dia de aula.
Os grupos devem enviar uma documentação técnica a respeito da solução criada. Sugestões de conteúdo da documentação técnica:

- Fornecer uma visão geral da solução criada e uma breve descrição das tecnologias utilizadas.
- Descrever a abordagem adotada para realização do projeto, incluindo as ferramentas e técnicas utilizadas.
- Detalhar quaisquer limitações ou suposições feitas durante o processo de desenvolvimento, destacando quaisquer pontos fortes ou fracos da tecnologia ou solução que foram utilizadas.
- Resumo das principais descobertas feitas durante o projeto e tirar conclusões sobre a viabilidade e o potencial da solução desenvolvida. Ele também deve destacar quaisquer recomendações para testes ou desenvolvimentos adicionais.

💯 **Critérios de avaliação**

- A qualidade e integridade dos entregáveis do projeto, como o relatório final e protótipo da solução.
- Capacidade do aluno em identificar e resolver problemas encontrados durante o projeto, como desafios técnicos.
- Capacidade do aluno em apresentar efetivamente seu projeto por meio do relatório técnico.
- Capacidade do aluno de refletir sobre sua experiência de projeto, incluindo seus sucessos e desafios, e de identificar áreas para aprendizado e crescimento futuros.

## Requisitos

- Python `v3.10.12`
- Pip `v23.2.1`
- Banco de dados MySQL

## Como rodar o projeto

- Crie um ambiente virtual: `python -m venv venv`
- Rode o ambiente virtual: `source venv/bin/activate`
- Instale as dependências: `pip install -r requirements.txt`
- Crie o arquivo `.env` com as variáveis de ambiente do banco de dados
- Rode o projeto: `python src/main.py`
