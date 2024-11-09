import { Routes, Route } from "react-router-dom"
import Home from "../pages/home-page"

export default function Router() {

  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  )
}