# import openai


# openai.api_key = open("key.txt", "r").read().strip("\n")

# question="مولانا جامی کیست؟"


# def answer(question):
#     completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages= [{"role": "user", "content": question}])
#     reply_content = completion["choices"][0].message.content
#     print(reply_content)

# answer(question)





from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(data):
    print(data)



if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app, host='0.0.0.0', port=8000, ssl_context=('server.crt', 'server.key'))



