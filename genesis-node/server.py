import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

load_dotenv()

GENESIS_IP = os.environ.get("VITE_GENESIS_SERVER", None)

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# Dictionary to store IP addresses with a counter as the key
ip_addresses = {}
node_counter = 0  # Initialize node counter


@socketio.on("connect")
def handle_connect():
    global node_counter  # To modify the global variable

    # Capture the IP address of the connected client
    ip_address = request.environ.get("REMOTE_ADDR")

    if ip_address in ip_addresses.values():
        socketio.emit("update_ip_addresses", ip_addresses)
        return

    # Store the IP address in the dictionary with the current counter as the key
    ip_addresses[node_counter] = ip_address
    node_counter += 1  # Increment the counter for the next entry

    print("Updated IP addresses:", ip_addresses)  # For server-side logging

    # Send the updated IP addresses to all connected clients
    socketio.emit("update_ip_addresses", ip_addresses)
    print("Client connected with IP:", ip_address)


@socketio.on("initiate_job")
def handle_update_ip(data):
    print(data)
    socketio.emit("start_job")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected.")


if __name__ == "__main__":
    socketio.run(app, host=GENESIS_IP, port=5000, debug=True)
