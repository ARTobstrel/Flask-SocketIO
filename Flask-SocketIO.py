#!/usr/bin/env python3

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app, async_mode='eventlet')

colors = {
    'red':128,
    'green':128,
    'blue':128
}

@app.route('/')
def index():
    text = 'Hello, my little friend. I am ancle'
    return render_template(
                            'index.html',
                            title='Main page',
                            text=text,
                            colors=colors
    )


if __name__ == '__main__':
    sio.run(app, debug=True)
