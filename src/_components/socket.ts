import { useEffect, useState, useCallback } from "react";
import { io } from "socket.io-client";
import api from "../api/api";

type IpAddress = { [idx: number]: string };

export const useSocket = (url: string) => {
  const [socket, setSocket] = useState(null);
  const [ipAddresses, setIpAddresses] = useState<IpAddress[]>([]);
  const [isConnected, setIsConnected] = useState(false);

  const [startJob] = api.endpoints.startJob.useMutation();

  useEffect(() => {
    const newSocket = io(url, { transports: ["websocket"] });
    setSocket(newSocket);

    newSocket.on("connect", () => {
      console.log("Connected to WebSocket server");
      setIsConnected(true);
    });

    // handle IP address updates from server
    newSocket.on("update_ip_addresses", (data) => {
      console.log(data);
      setIpAddresses(data);
    });

    newSocket.on("start_job", (data) => {
      console.log("starting local job");
      startJob(ipAddresses);
    });

    newSocket.on("disconnect", () => {
      console.log("Disconnected from WebSocket server");
      setIsConnected(false);
    });

    return () => newSocket.close();
  }, [url]);

  const sendMessage = useCallback(
    (proto, msg) => {
      if (socket) socket.emit(proto, msg);
    },
    [socket]
  );

  return { isConnected, ipAddresses, sendMessage };
};
