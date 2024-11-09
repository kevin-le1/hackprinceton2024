from flask import Flask, request, jsonify

app = Flask(__name__)

# A dictionary to store IP addresses with a counter as the key
ip_addresses = {}
node_counter = 0  # Initialize node counter

@app.route('/add_ip', methods=['POST'])
def receive_ip():
    global node_counter  # To modify the global variable
    ip_address = request.remote_addr
    # Store the IP address in the dictionary with the current counter as the key
    ip_addresses[node_counter] = ip_address
    node_counter += 1  # Increment the counter for the next entry
    print(ip_addresses)
    # Return a success message along with the IP address
    return jsonify({'status': 'success', 'node number': node_counter, 'ip': ip_address}), 200

if __name__ == '__main__':
    app.run(debug=True, host="10.49.158.119", port=5000)
