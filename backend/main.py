from fastapi import FastAPI
from fastapi.websockets import WebSocket
from chat import chat_handler

app = FastAPI()

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await chat_handler(websocket)