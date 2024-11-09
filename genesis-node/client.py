import socketio

# Initialize Socket.IO client
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server.")

@sio.event
def update_ip_addresses(data):
    print("Updated IP addresses:", data)

@sio.event
def disconnect():
    print("Disconnected from the server.")

# Connect to the server (replace <server_ip> with the actual server IP)
sio.connect("http://10.49.158.119:5000")
sio.wait()

