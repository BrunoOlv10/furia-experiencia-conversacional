import emoji
import os
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi.concurrency import run_in_threadpool
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

async def ask_gemini(question: str) -> str:
    try:
        # response = model.generate_content(question)
        response = await run_in_threadpool(model.generate_content, question)
        return response.text
    except Exception as e:
        return f"Erro ao retornar a resposta: {str(e)}"

async def chat_handler(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            message = (await websocket.receive_text()).strip().lower()
            print(f"Mensagem recebida: {message}")
            
            if message.lower() in ["oi", "olá", "fala furia", "e aí"]:
                await websocket.send_text(
                    emoji.emojize(
                        ":paw_prints: Fala, guerreiro(a)! Quer ficar por dentro de tudo da FURIA? Digite um número:\n" 
                        ":keycap_1: - História da Furia \n" 
                        ":keycap_2: - Nossos Times \n" 
                        ":keycap_3: - Últimos Jogos \n" 
                        ":keycap_4: - Próximos Jogos \n" 
                        ":keycap_5: - Lojinha da Pantera \n" 
                        ":keycap_6: - Esports News \n" 
                        ":keycap_7: - Criadoras de conteúdo e Streamers"
                    )
                )
            elif message == "1":
            # if message == "1":
                # response = await ask_gemini("Conte a história, brevemente, do time da FURIA Esports.")
                response = "teste"
                await websocket.send_text(emoji.emojize(f":open_book: Nossa história:\n{response}"))
            elif message == "2":
                # response = await ask_gemini("Quais são, em lista e brevemente, os times da FURIA Esports?")
                await websocket.send_text(emoji.emojize(f":handshake: Nossos times:\n{response}"))
            elif message == "3":
                # response = await ask_gemini("Quais foram os últimos jogos da FURIA Esports? Me dê detalhes, em lista e brevemente, dele(s).")
                await websocket.send_text(emoji.emojize(f":calendar: Últimos jogos:\n{response}"))
            # elif message == "4":
                # response = await ask_gemini("Quais são os próximos jogos da FURIA Esports? Me dê detalhes, em lista e brevemente, dele(s).")
                # await websocket.send_text(emoji.emojize(f":calendar: Próximos jogos:\n{response}"))
            elif message == "5":
                await websocket.send_text(emoji.emojize(":shopping_cart: Lojinha da pantera: Acompanhe aqui https://www.furia.gg"))
            elif message == "6":
                # response = await ask_gemini("Quais são, em lista e brevemente, as últimas notícias sobre Esports da Fúria? Utilize como fonte o 'ge'.")
                await websocket.send_text(emoji.emojize(f":newspaper: Esports News:\n{response}"))
            elif message == "7":
                # response = await ask_gemini("Quais são, em lista e brevemente, os criadores de conteúdo e streamers da FURIA Esports?")
                await websocket.send_text(emoji.emojize(f":video_game: Criadores de Conteúdo:\n{response}"))
            else:
                await websocket.send_text(
                    "🤖 Não entendi... tente digitar algumas das opções (1, 2 etc...)."
                )
    except WebSocketDisconnect:
        print("Cliente desconectado")