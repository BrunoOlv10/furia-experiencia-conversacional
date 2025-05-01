import emoji
from fastapi.websockets import WebSocket, WebSocketDisconnect

async def chat_handler(websocket: WebSocket):
    await websocket.accept() 
    try:
        while True:
            message = (await websocket.receive_text()).strip().lower()
            print(f"Mensagem recebida: {message}")
            
            if message.lower() in ["oi", "olá", "fala furia", "e aí"]:
                await websocket.send_text(
                    emoji.emojize(":paw_prints: Fala, guerreiro(a)! Quer ficar por dentro de tudo da FURIA? Digite um número:\n :keycap_1: - História da Furia \n :keycap_2: - Nossos times \n :keycap_3: - Jogos ao vivo \n :keycap_4: - Próximos jogos \n :keycap_5: - Lojinha da pantera \n :keycap_6: - Esports News \n :keycap_7: - Criadoras de conteúdo e Streamers")
                )
            elif message == "1":
                await websocket.send_text(
                    "⚡ Nossa história: HISTÓRIA"
                )
            elif message == "2":
                await websocket.send_text(
                    "⚡ Nossos times: TIMES"
                )
            elif message == "3":
                await websocket.send_text(
                    "⚡ Jogos ao vivo: Acompanhe aqui https://furia.gg/agenda"
                )
            elif message == "4":
                await websocket.send_text(
                    "⚡ Próximos jogos: Acompanhe aqui https://furia.gg/agenda"
                )
            elif message == "5":
                await websocket.send_text(
                    "⚡ Lojinha da pantera: Acompanhe aqui https://www.furia.gg"
                )
            elif message == "6":
                await websocket.send_text(
                    "⚡ Esports News: NEWS"
                )
            elif message == "7":
                await websocket.send_text(
                    "⚡ Criadoras de conteúdo e Streamers: PESSOAS"
                )
            else:
                await websocket.send_text(
                    "🤖 Não entendi... tente digitar algumas das opções (1, 2 etc...)."
                )
    except WebSocketDisconnect:
        print("Cliente desconectado")