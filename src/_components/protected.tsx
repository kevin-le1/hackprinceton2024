import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { useNavigate } from "react-router-dom";

interface DefaultProps {
  children: React.ReactNode;
}

export default function Protected({ children }: DefaultProps) {
  const navigate = useNavigate();
  // const [tokenIsSaved, setTokenIsSaved] = React.useState(false);

  // use Auth0 user in the future, but ignore for now
  const { isAuthenticated, getIdTokenClaims } = useAuth0();

  React.useEffect(() => {
    async function saveToken() {
      const tokenExists = localStorage.getItem("authToken") != null;
      if (tokenExists) return;

      try {
        const token = await getIdTokenClaims();
        if (!token || !token.__raw) return;
        localStorage.setItem("authToken", token?.__raw);
        // setTokenIsSaved(true);
      } catch (e) {
        console.log(e);
      }
    }

    if (isAuthenticated) saveToken();
  }, [isAuthenticated, getIdTokenClaims]);

  if (!isAuthenticated) navigate("/");

  return children;
}
