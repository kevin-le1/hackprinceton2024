import { Routes, Route } from "react-router-dom";
import Input from "../pages/input-page";
import Dash from "../pages/dash-page";
import { ReactElement } from "react";
import Home from "../pages/home-page";
import Protected from "../_components/protected";

interface RouteDef {
  path: string;
  component: ReactElement;
  protected?: boolean;
}

const routes: RouteDef[] = [
  { path: "/", component: <Home />, protected: false },
  //
  { path: "/patients", component: <Input /> },
  { path: "/dashboard", component: <Dash /> },
];

export default function Router() {
  return (
    <Routes>
      {routes.map((route) => {
        const isProtected = route.protected ?? true;
        const component = isProtected ? (
          <Protected>{route.component}</Protected>
        ) : (
          route.component
        );
        return <Route path={route.path} element={component} />;
      })}
    </Routes>
  );
}
