# 🐾 FURIA Esports Chat — Angular + Python + Gemini AI

Projeto de chat interativo para fãs da FURIA Esports, com interface em Angular, back-end em Python e integração com a IA Gemini (Google). A aplicação responde em tempo real via WebSocket, permitindo uma experiência agradável e informativa sobre o time e sua comunidade.

---

## 🎯 Funcionalidades

- Chat com inteligência artificial (Gemini AI)
- Comunicação em tempo real via WebSocket
- Interface com 6 opções de interação: <br>
    1- História da FURIA <br>
    2- Nossos Times <br>
    3- Últimos Jogos <br>
    4- Lojinha da Pantera <br>
    5- Esports News <br>
    6- Criadores de Conteúdo
- Respostas com texto formatado (negrito, emojis, links)

---

## 📁 Estrutura do Projeto

```
/
├── backend/ # Python + Gemini
└── frontend/chat/ # Interface Angular
```

---

## 🧠 Back-end — Python

### Tecnologias

- Python
- FastAPI
- WebSocket
- Gemini API (Google Generative AI)
- Dotenv
- emoji

### Executar localmente

```bash
1. Acesse a pasta backend:
cd backend

2. Crie um arquivo .env dentro da pasta backend contendo:
GEMINI_API_KEY=sua-chave-aqui

OBS: ⚠️ A chave da Gemini API pode ser obtida em: https://aistudio.google.com/app/apikey

3. Instalar as dependências:
pip install -r requirements.txt

4. Inicie o servidor:
uvicorn main:app --reload
```

### WebSocket (opcional) - Teste isolado da comunicação do chat

```bash
1. Acesse a pasta backend:
cd backend

2. Rodar o endpoint:
websocat ws://localhost:8000/ws
```
---

## 🖥️ Front-end — Angular
### Tecnologias

- Angular
- TypeScript
- SCSS
- WebSocket

### Executar localmente

```bash
1. Acesse a pasta do front-end:
cd frontend/chat

2. Instale as dependências:
npm install

3. Rode a aplicação:
ng serve
```

---

## 🌐 Acesso em produção

👉 Acesse: https://furia-chat-experiencia-conversacional.vercel.app

O front-end Angular está hospedado no Vercel e se conecta ao back-end Python publicado no Render.

---

## 🧪 Como Testar

- Opção 1: acesse diretamente o link do front-end publicado no Vercel, já conectado ao back-end.
- Opção 2: rode o back-end localmente com uvicorn e o front-end com ng serve. Não se esqueça de instalar as dependências e a chave da API Gemini conforme explicado anteriormente.
- Teste as opções do menu e veja as respostas da IA.
