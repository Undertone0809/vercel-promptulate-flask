from flask import Flask, request
from promptulate.llms import ChatOpenAI

app = Flask(__name__)


@app.get("/api/hello")
def hello():
    return "Hello Promptulate!"


@app.post("/api/chat")
def chat():
    json_data = request.get_json()
    prompt = json_data.get("prompt")
    llm = ChatOpenAI()
    return {"answer": llm(prompt)}
