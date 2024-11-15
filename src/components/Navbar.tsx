import { Button } from "./ui/button";
import { useAuth0 } from "@auth0/auth0-react";
import { useNavigate } from "react-router-dom";

export default function Navbar({ pageType }: any) {
  const { loginWithRedirect, logout, isLoading, isAuthenticated } = useAuth0();

  const handleLogin = async () => {
    await loginWithRedirect({
      appState: {
        returnTo: "/dashboard",
      },
    });
  };

  const handleSignup = async () => {
    await loginWithRedirect({
      authorizationParams: {
        screen_hint: "signup",
      },
      appState: {
        returnTo: "/dashboard",
      },
    });
  };

  const handleLogout = () => {
    logout({ returnTo: window.location.origin });
  };

  if (pageType === "home") {
    return (
      <nav className="fixed inset-x-0 top-0 z-50 bg-primary shadow-sm dark:bg-gray-950/90">
        <div className="w-full max-w-7xl mx-auto px-4">
          <div className="flex justify-between h-14 items-center">
            <a href="/" className="flex items-center">
              <div className = "text-white font-extrabold hover:text-slate-200 pr-2">HealthSync </div>
              <MountainIcon className="h-6 w-6" />
              <span className="sr-only">HC Project</span>
            </a>
            <nav className="hidden md:flex gap-4"></nav>
            <div className="flex items-center gap-4">
              <Button
                variant="outline"
                size="sm"
                className="text-black hover:text-white hover:bg-stone-900"
                onClick={handleLogin}
              >
                Login
              </Button>
              <Button
                className="text-black hover:text-white hover:bg-stone-900 bg-white"
                size="sm"
                onClick={handleSignup}
              >
                Sign up
              </Button>
            </div>
          </div>
        </div>
      </nav>
    );
  }

  const navigate = useNavigate();

  if (pageType === "input") {
    if (!isAuthenticated && !isLoading) {
      navigate("/");
    }
    return (
      <nav className="fixed inset-x-0 top-0 z-50 bg-primary shadow-sm dark:bg-gray-950/90">
        <div className="w-full max-w-7xl mx-auto px-4">
          <div className="flex justify-between h-14 items-center">
            <a href="/" className="flex items-center">
            <div className = "text-white font-extrabold hover:text-slate-200 pr-2">HealthSync </div>
              <MountainIcon className="h-6 w-6" />
              <span className="sr-only">HC Project</span>
            </a>
            <nav className="hidden md:flex gap-4">
              <a
                href="/dashboard"
                className={`text-white font-extrabold hover:text-slate-200 ${
                  pageType === "dash" ? "underline" : ""
                }`}
              >
                Dashboard
              </a>
              <div className="font-extrabold">|</div>{" "}
              {/* Vertical line separator */}
              <a
                href="/patients"
                className={`text-white font-extrabold hover:text-slate-200 ${
                  pageType === "input" ? "underline" : ""
                }`}
              >
                Patients
              </a>
            </nav>
            <div className="flex items-center gap-4">
              <>
                <Button
                  variant="outline"
                  size="sm"
                  className="text-black hover:text-white hover:bg-stone-900"
                  onClick={handleLogout}
                >
                  Logout
                </Button>
              </>
            </div>
          </div>
        </div>
      </nav>
    );
  }

  if (pageType === "dash") {
    if (!isAuthenticated && !isLoading) {
      navigate("/");
    }
    return (
      <nav className="fixed inset-x-0 top-0 z-50 bg-primary shadow-sm dark:bg-gray-950/90">
        <div className="w-full max-w-7xl mx-auto px-4">
          <div className="flex justify-between h-14 items-center">
            <a href="/" className="flex items-center">
            <div className = "text-white font-extrabold hover:text-slate-200 pr-2">HealthSync </div>
              <MountainIcon className="h-6 w-6" />
              <span className="sr-only">HC Project</span>
            </a>
            <nav className="hidden md:flex gap-4">
              <a
                href="/dashboard"
                className={`text-white font-extrabold hover:text-slate-200 ${
                  pageType === "dash" ? "underline" : ""
                }`}
              >
                Dashboard
              </a>
              <div className="font-extrabold">|</div>{" "}
              {/* Vertical line separator */}
              <a
                href="/patients"
                className={`text-white font-extrabold hover:text-slate-200 ${
                  pageType === "input" ? "underline" : ""
                }`}
              >
                Patients
              </a>
            </nav>
            <div className="flex items-center gap-4">
              <>
                <Button
                  variant="outline"
                  size="sm"
                  className="text-black hover:text-white hover:bg-stone-900"
                  onClick={handleLogout}
                >
                  Logout
                </Button>
              </>
            </div>
          </div>
        </div>
      </nav>
    );
  }
}

function MountainIcon(props: any) {
  return (
    <img
      {...props}
      src="src/images/healthsync-logo.png"
      alt="HealthSync Logo"
      width="24"
      height="24"
    />
  );
}
