import React from "react";
import { useSocket } from "./socket";
import { Button } from "../components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../components/ui/table";

function JoinNetwork() {
  const { isConnected, ipAddresses, sendMessage } = useSocket(
    `http://${import.meta.env.VITE_GENESIS_SERVER}:5000`
  );

  console.log("ip", ipAddresses.current);

  return (
    <Card  className="w-[400px] shadow-lg">
      <CardHeader>
        <CardTitle className="flex items-center gap-4">
          Network Status
          <Badge variant={isConnected ? "default" : "destructive"}>
            {isConnected ? "Connected" : "Disconnected"}
          </Badge>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Button
          onClick={() => sendMessage("initiate_job", null)}
          variant="default"
          className="w-full"
          disabled={!isConnected}
        >
          Calculate Schedulings
        </Button>

        {isConnected && (
          <div>
            <h3 className="text-sm font-semibold mb-2">Connected Peers</h3>
            <div className="border rounded-md max-h-[200px] overflow-auto">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>IP Address</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {Object.values(ipAddresses.current)?.map((address, index) => (
                    <TableRow key={index}>
                      <TableCell>{address}</TableCell>
                    </TableRow>
                  ))}
                  {(!ipAddresses ||
                    Object.values(ipAddresses).length === 0) && (
                    <TableRow>
                      <TableCell className="text-center text-muted-foreground">
                        No peers connected
                      </TableCell>
                    </TableRow>
                  )}
                </TableBody>
              </Table>
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
}

export default JoinNetwork;
