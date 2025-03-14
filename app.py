from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable WebSockets

@app.route("/")
def index():
    return render_template("index.html")  # Serve the HTML page

# Handle WebSocket messages
@socketio.on("message")
def handle_message(msg):
    print(f"Message received: {msg}")
    send(f"Broadcast: {msg}", broadcast=True)  # Send message to all clients

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
