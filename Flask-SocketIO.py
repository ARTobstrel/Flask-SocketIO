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

@app.route('/remote')
def remote():
    return render_template('remote.html', colors=colors)

@sio.on('colors', namespace='/flask')
def change_colors(msg):
    global colors

    colors[msg['color']] = msg['value']
    sio.emit('square', colors, namespace='/flask')

if __name__ == '__main__':
    sio.run(app, debug=True)
