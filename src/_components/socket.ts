import { useEffect, useState, useCallback, useRef } from "react";
import { io, Socket } from "socket.io-client";
import api from "../api/api";

export type IpAddress = { [idx: number]: string };

export const useSocket = (url: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  // const [ipAddresses, setIpAddresses] = useState<IpAddress[]>([]);
  const [isConnected, setIsConnected] = useState(false);

  const ipAddresses = useRef<IpAddress>([]);

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
      console.log("updating ip", data);
      ipAddresses.current = data;
      // console.log(ipAddresses.current);
      // setIpAddresses(data);
    });

    newSocket.on("start_job", (data) => {
      console.log("starting local job", ipAddresses);
      startJob({ ipAddresses: ipAddresses.current });
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
