import emoji
import os
import re
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi.concurrency import run_in_threadpool
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def format_response(response_text: str) -> str:
    response_text = response_text.replace("\n", "<br>")
    
    url_pattern = re.compile(r'https?://\S+')
    response_text = re.sub(url_pattern, r'<a href="\g<0>" target="_blank">\g<0></a>', response_text)
    
    return response_text

async def ask_gemini(question: str) -> str:
    try:
        response = await run_in_threadpool(model.generate_content, question)
        return response.text
    except Exception as e:
        return f"Erro ao retornar a resposta: {str(e)}"
    
MENU_OPTIONS = emoji.emojize(
    ":keycap_1: História da FURIA \n"
    ":keycap_2: Nossos Times \n"
    ":keycap_3: Últimos Jogos \n"
    ":keycap_4: Lojinha da Pantera \n"
    ":keycap_5: Esports News \n"
    ":keycap_6: Criadores de Conteúdo"
)
    
MENU_MESSAGE = emoji.emojize(
    f":paw_prints: Digite um número:\n{MENU_OPTIONS}"
)

INITIAL_MESSAGE = emoji.emojize(
    f":paw_prints: Fala, guerreiro(a)! Quer ficar por dentro de tudo da FURIA? \nDigite um número:\n{MENU_OPTIONS}"
)

async def chat_handler(websocket: WebSocket):
    await websocket.accept()
    primeira_interacao = True
    try:
        while True:
            message = (await websocket.receive_text()).strip().lower()
            print(f"Mensagem recebida: {message}")

            if primeira_interacao:
                await websocket.send_text(format_response(INITIAL_MESSAGE))
                primeira_interacao = False
    
            elif message == "1":
                response = await ask_gemini("Conte a história, brevemente, do time da FURIA Esports.")
                await websocket.send_text(format_response(emoji.emojize(f":open_book: Nossa história:\n{response}")))
                await websocket.send_text(format_response(MENU_MESSAGE))

            elif message == "2":
                response = await ask_gemini("Quais são, em lista e brevemente, os times da FURIA Esports?")
                await websocket.send_text(format_response(emoji.emojize(f":handshake: Nossos times:\n{response}")))
                await websocket.send_text(format_response(MENU_MESSAGE))

            elif message == "3":
                response = await ask_gemini("Quais foram os últimos jogos da FURIA Esports? Me dê detalhes, em lista e brevemente, dele(s).")
                await websocket.send_text(format_response(emoji.emojize(f":calendar: Últimos jogos:\n{response}")))
                await websocket.send_text(format_response(MENU_MESSAGE))

            elif message == "4":
                await websocket.send_text(format_response(emoji.emojize(":shopping_cart: Lojinha da pantera: https://www.furia.gg")))
                await websocket.send_text(format_response(MENU_MESSAGE))

            elif message == "5":
                response = await ask_gemini("Quais são, em lista e brevemente, as últimas notícias sobre Esports da Fúria? Utilize como fonte o 'ge'.")
                await websocket.send_text(format_response(emoji.emojize(f":newspaper: Esports News:\n{response}")))
                await websocket.send_text(format_response(MENU_MESSAGE))

            elif message == "6":
                response = await ask_gemini("Quais são, em lista e brevemente, os criadores de conteúdo e streamers da FURIA Esports?")
                await websocket.send_text(format_response(emoji.emojize(f":video_game: Criadores de Conteúdo:\n{response}")))
                await websocket.send_text(format_response(MENU_MESSAGE))

            else:
                await websocket.send_text(emoji.emojize(":robot: Não entendi, guerreiro(a)... Tente digitar algumas das opções disponíveis (1-6)."))
                await websocket.send_text(format_response(MENU_MESSAGE))

    except WebSocketDisconnect:
        print("Cliente desconectado")