from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins

# Dictionary to store IP addresses with a counter as the key
ip_addresses = {}
node_counter = 0  # Initialize node counter

@socketio.on('connect')
def handle_connect():
    global node_counter  # To modify the global variable

    # Capture the IP address of the connected client
    ip_address = request.environ.get('REMOTE_ADDR')
    
    # Store the IP address in the dictionary with the current counter as the key
    ip_addresses[node_counter] = ip_address
    node_counter += 1  # Increment the counter for the next entry

    print("Updated IP addresses:", ip_addresses)  # For server-side logging
    
    # Send the updated IP addresses to all connected clients
    socketio.emit('update_ip_addresses', ip_addresses)
    print("Client connected with IP:", ip_address)

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected.")

if __name__ == '__main__':
    # Run the WebSocket server
    socketio.run(app, host="10.49.158.119", port=5000, debug=True)
