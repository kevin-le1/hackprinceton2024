import React from "react";
import { useSocket } from "./socket";

function JoinNetwork() {
  const { isConnected, ipAddresses, sendMessage } = useSocket(
    "http://localhost:5000"
  );

  const handleSendMessage = () => {
    sendMessage("initiate_job", null);
  };

  return (
    <div>
      <h1>WebSocket Status: {isConnected ? "Connected" : "Disconnected"}</h1>
      <button onClick={handleSendMessage}>Send Message</button>
      <h2>Received IP Addresses:</h2>
      <pre>{JSON.stringify(ipAddresses, null, 2)}</pre>
    </div>
  );
}

export default JoinNetwork;
