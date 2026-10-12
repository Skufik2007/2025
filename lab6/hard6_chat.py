# Повышенное задание 6. Приложение чат (WebSocket FastAPI)
# Запуск: uvicorn hard6_chat:app --reload, открыть http://127.0.0.1:8000 в двух вкладках
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()
clients = []

html = """
<!doctype html>
<html><head><meta charset="utf-8"><title>Чат</title></head>
<body>
<h2>Чат</h2>
<input id="msg"><button onclick="send()">Отправить</button>
<ul id="messages"></ul>
<script>
  var ws = new WebSocket("ws://" + location.host + "/ws");
  ws.onmessage = function(event) {
    var li = document.createElement("li");
    li.textContent = event.data;
    document.getElementById("messages").appendChild(li);
  };
  function send() {
    var input = document.getElementById("msg");
    ws.send(input.value);
    input.value = "";
  }
</script>
</body></html>
"""


@app.get("/")
def page():
    return HTMLResponse(html)


@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            text = await websocket.receive_text()
            for client in clients:
                await client.send_text(text)
    except WebSocketDisconnect:
        clients.remove(websocket)
