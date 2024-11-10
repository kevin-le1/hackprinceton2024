import subprocess
import flask
from flask_smorest import Blueprint
from flask import jsonify, request
from concurrent.futures import ThreadPoolExecutor, as_completed

ns = Blueprint("job", "job", url_prefix="/job", description="job")

# Create a thread pool executor
executor = ThreadPoolExecutor(max_workers=5)


def run_command(command, ip):
    """Helper function to execute a command asynchronously and capture output."""
    try:
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Collect and print output line by line
        stdout_lines, stderr_lines = [], []
        for stdout_line in process.stdout:
            stdout_lines.append(stdout_line)
            print(stdout_line, end="")

        # Ensure subprocess completion
        process.stdout.close()
        process.wait()

        # Capture and print any stderr lines
        for stderr_line in process.stderr:
            stderr_lines.append(stderr_line)
            print(stderr_line, end="")

        return stdout_lines, stderr_lines
    except Exception as e:
        print(f"Error executing command for IP {ip}: {e}")
        return [], [str(e)]


def consensus(ip_addresses):
    """
    Generates a consensus command for each IP in the ip_addresses dictionary.
    Invokes each command asynchronously.
    """
    ip = request.environ.get("REMOTE_ADDR")
    index = int("".join([k for k, v in ip_addresses.items() if ip == v]))

    # Build the command
    command = ["poetry", "run", "python", "smc_test/main.py", f"-I{index}"]

    # Add each IP to the command, setting localhost for the current IP
    for other_index, other_ip in ip_addresses.items():
        if other_index == index:
            command.extend(["-P", "localhost"])
        else:
            command.extend(["-P", other_ip])

    command.extend(["-ll", "debug"])
    print(f"Executing command for IP {ip}: {' '.join(command)}")

    # Run command asynchronously in a thread pool
    future = executor.submit(run_command, command, ip)
    return future  # Return the future for tracking


@ns.route("/start", methods=["POST"])
def start_job():
    """Endpoint to trigger the consensus process with IP addresses from the request body."""
    try:
        # Get IP addresses from the POST request JSON data
        ip_addresses = request.json.get("ipAddresses")

        # Ensure IP addresses are provided in the request
        if not ip_addresses:
            return jsonify(
                {"status": "error", "message": "IP addresses are required"}
            ), 400

        # Trigger the consensus process
        future = consensus(ip_addresses)

        # Optionally, track if the job started successfully
        if future:
            return jsonify(
                {"status": "success", "message": "Consensus triggered successfully"}
            ), 200
        else:
            return jsonify(
                {"status": "error", "message": "Failed to start consensus"}
            ), 500

    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 500
