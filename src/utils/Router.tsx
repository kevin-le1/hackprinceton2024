import { Routes, Route } from "react-router-dom"
import Home from "../pages/home-page"
import Input from "../pages/input-page"
import Dash from "../pages/dash-page"

export default function Router() {

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/input" element={<Input />} />
      <Route path="/dash" element={<Dash />} />
    </Routes>
  )
}