import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "../components/ui/button";
// import React from "react";

export default function Home() {

    const { loginWithRedirect } = useAuth0();

    const handleLogin = async () => {
        await loginWithRedirect({
            appState: {
            returnTo: "/input",
            },
        });
    };

    return (
        <div className="flex items-center justify-center min-h-screen min-w-screen bg-black text-gray-800 p-4">
                <Button className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-lg transition ease-in-out duration-200 w-auto" onClick={() => handleLogin()}>
                    Login / Sign Up
                </Button>
        </div>
    );
}
