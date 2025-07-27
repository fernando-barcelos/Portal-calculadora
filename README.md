# 🧮 Calculadora Web com Django

Este projeto é uma calculadora digital criada como uma aplicação web utilizando **Django** no backend e **JavaScript** para a lógica da calculadora no frontend. Ele permite que usuários se cadastrem, façam login e realizem operações matemáticas básicas, com histórico de uso.

---

## 🚀 Funcionalidades

- Cadastro de usuário com e-mail e senha
- Login seguro utilizando e-mail e senha
- Interface de calculadora interativa com lógica feita em JavaScript
- Armazenamento das operações realizadas no banco de dados
- Exibição dos **3 últimos registros** de operações realizadas
- Duas tabelas principais:
  - `Usuários`: Armazena dados de login
  - `Operações`: Registra os cálculos feitos pelos usuários

---

## 🛠 Tecnologias Utilizadas

- **Backend**: Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de dados**: SQLite (padrão)
- **Controle de versão**: Git

---

## 📦 Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. **Crie um ambiente virtual:**
    python -m venv venv

3. **Ative o ambiente virtual:**
    Windows: venv\Scripts\activate
    Linux/macOS: source venv/bin/activate

4. **Instale as dependências do projeto:**
    pip install -r requirements.txt

5. **Realize as migrações e inicie o servidor:**
    python manage.py migrate
    python manage.py runserver