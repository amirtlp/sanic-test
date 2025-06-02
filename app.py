# app.py
from sanic import Sanic
from sanic.response import json, text
from config import HOST, PORT, DEBUG, WORKERS

app = Sanic("TestApp")

@app.get("/")
async def index(request):
    return text("Hello from Sanic! You can access this endpoint.")

@app.post("/hello")
async def hello(request):
    data = request.json
    name = data.get("name", "World")
    return json({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        workers=WORKERS,
        auto_reload=False
    )