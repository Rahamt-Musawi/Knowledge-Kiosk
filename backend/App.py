from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import openai
openai.api_key = open("key.txt", "r").read().strip("\n")

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


def answer(question):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [{"role": "user", "content": question}])
    reply_content = completion["choices"][0].message.content
    print(reply_content)
    emit('response', {'data': reply_content})

@socketio.on('question')
def handle_message(question):
    print('Question:', question)
    print()
    answer(question)


if __name__ == '__main__':
    socketio.run(app)

