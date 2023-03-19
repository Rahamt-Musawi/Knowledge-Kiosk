import socketio
import eventlet
sio = socketio.Server()

@sio.event
def message(sid, data):
    print(data)

app = socketio.WSGIApp(sio)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
