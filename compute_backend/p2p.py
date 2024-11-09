from pythonp2p import Node
import threading

# Define a custom ChatNode class that extends the Node class
class ChatNode(Node):
    def __init__(self, host, port, file_port):
        super().__init__(host, port, file_port)
        self.id = self.id  # Unique identifier for this node

    # Override the on_message function to display received messages
    def on_message(self, message, sender, private):
        print(f"\nReceived message from {sender}: {message}")
        if private:
            print("[Private Message]")

    # Function to send messages to a specific receiver
    def send_chat_message(self, message, receiver=None):
        self.send_message({"message": message}, receiver)
        print(f"Sent message: {message}")

# Function to start the node and manage connections
def start_chat_node(host, port, file_port, connect_to_ip=None):
    node = ChatNode(host, port, file_port)
    node.start()  # Start the node to begin listening

    # If there's a peer to connect to, initiate connection
    if connect_to_ip:
        node.connect_to(connect_to_ip, port)

    # Separate thread for message input
    def send_messages():
        while True:
            message = input("\nEnter message: ")
            receiver = input("Enter receiver ID (leave blank for broadcast): ")
            receiver = receiver if receiver else None
            node.send_chat_message(message, receiver)

    # Run the send_messages function in a new thread
    threading.Thread(target=send_messages).start()

# Example usage
# Start the chat node with host, port, and file port; set connect_to_ip for the second node to connect to the first
if __name__ == "__main__":
    host = "10.49.158.119"  # Local IP for the first node
    port = 65432            # Default port for chat
    file_port = 65433       # Default file transfer port

    # Start the first node without a connect_to_ip argument
    start_chat_node(host, port, file_port)
