import socketio
import subprocess
from flask import Flask, request, jsonify

# Initialize Flask app for exposing the consensus endpoint
app = Flask(__name__)

def consensus(ip_addresses):
    """
    Generates a consensus command for each IP in the ip_addresses dictionary.
    Invokes each command using subprocess.
    """
    for index, ip in ip_addresses.items():
        # Build the command
        command = ["python", "file.py", f"-I{index}"]
        
        # Add each IP to the command, setting localhost for the current IP
        for other_index, other_ip in ip_addresses.items():
            if other_index == index:
                command.extend(["-P", "localhost"])
            else:
                command.extend(["-P", other_ip])

        print(f"Executing command for IP {ip}: {' '.join(command)}")
        
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error executing command for IP {ip}: {e}")

@app.route('/consensus', methods=['POST'])
def trigger_consensus():
    """Endpoint to trigger the consensus process with IP addresses from the request body."""
    try:
        # Get IP addresses from the POST request JSON data
        ip_addresses = request.json.get('ip_addresses')
        
        # Ensure IP addresses are provided in the request
        if not ip_addresses:
            return jsonify({'status': 'error', 'message': 'IP addresses are required'}), 400

        # Trigger the consensus process
        consensus(ip_addresses)
        return jsonify({'status': 'success', 'message': 'Consensus triggered successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask server for the consensus endpoint
    app.run(port=8000)  # Expose on port 8000
