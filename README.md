# 🚀 FastAPI + PostgreSQL + Docker Starter Kit

Um template completo para desenvolvimento de APIs com FastAPI, PostgreSQL e Docker com todas as configurações necessárias.

## 📋 Pré-requisitos

- Python 3.10+
- Docker e Docker Compose instalados
- Pip atualizado

## 🛠️ Configuração Inicial

## Instalar Pipenv
pip install pipenv --user
## Atualizar pip
python -m pip install --upgrade pip
## Ativar ambiente virtual
pipenv shell
## Instalar as depedências
pipenv install -r requirements.txt
## Rodar projeto
uvicorn main:app --port 8080 --reload - acesse http://localhost:8080/docs para validar
## Subir containers
Na pasta raiz do projeto executar docker-compose up -d
## Criar tabelas
Na raiz do projeto rodar python utils/init_db.py
## Registrar banco
Através do PGAdmin (localhost:5050 - user = admin@gmail e senha = admin) registre um serve com nome todo_list, hostname postgresql, user e senha admin.
## Popular tabelas
Da maneira que preferir popule o banco com o script localizado na raiz do projeto - massa.sql
## Testar endpoinb de login
Username = johndoe e senha = secret




