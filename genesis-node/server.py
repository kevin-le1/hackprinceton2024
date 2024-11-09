from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)  # Initialize SocketIO with Flask

# Dictionary to store IP addresses with a counter as the key
ip_addresses = {}
node_counter = 0  # Initialize node counter

@app.route('/add_ip', methods=['POST'])
def receive_ip():
    global node_counter  # To modify the global variable
    ip_address = request.remote_addr
    
    # Store the IP address in the dictionary with the current counter as the key
    ip_addresses[node_counter] = ip_address
    node_counter += 1  # Increment the counter for the next entry
    print(ip_addresses)  # For server-side logging
    
    # Broadcast the updated IP addresses to all connected clients
    socketio.emit('update_ip_addresses', ip_addresses)
    
    return jsonify({'status': 'success', 'node number': node_counter, 'ip': ip_address}), 200

@socketio.on('connect')
def handle_connect():
    # Send the current IP addresses to the newly connected client
    emit('update_ip_addresses', ip_addresses)

if __name__ == '__main__':
    # Use eventlet as the WebSocket server
    socketio.run(app, host="10.49.158.119", port=5000, debug=True)
