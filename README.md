# 🧠 300 Simple Words

Uma aplicação web interativa para adicionar, classificar e salvar frases em inglês com explicações detalhadas — ideal para estudantes, professores e apaixonados por linguagem!

## 🚀 Funcionalidades

- ✅ Adição de frases com palavra-chave, tipo gramatical e explicação
- ✅ Classificação por Substantivo, Verbo ou Adjetivo
- ✅ Painel de frases salvas com visualização rápida
- ✅ Integração com API de voz (Azusse) para leitura das frases
- ✅ Painel administrativo para gerenciar dados e chaves de API

## 🖼️ Layout

A interface é dividida em duas seções:
- **Adicionar Frase**: formulário intuitivo com campos bem definidos
- **Frases Salvas**: painel dinâmico com frases já cadastradas

## 🛠️ Tecnologias utilizadas

- Python 3.13
- Django 5.2
- HTML5 + CSS3
- SQLite (desenvolvimento)
- Azusse Speech API (integração de voz)

## ⚙️ Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/300_simple_words.git
cd 300_simple_words

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário para acessar o admin
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
