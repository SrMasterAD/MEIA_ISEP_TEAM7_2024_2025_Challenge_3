// src/App.tsx
import { Routes, Route, useLocation } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Configurations from "./pages/Configurations";
import Banner from "./components/Banner";
import Navbar from "./components/Navbar";
import Register from "./pages/Register";
import ProtectedRoute from "./security/ProtectedRoute";
import Footer from "./components/Footer";

export default function App() {
  const location = useLocation();
  const isLoginPage = location.pathname === "/login";
  const isRegisterPage = location.pathname === "/register";

  return (
    <div className="min-h-screen px-1 flex flex-col">
      <Banner />
      {!isLoginPage && !isRegisterPage && <Navbar />}

      <main className="flex-1 p-4">
        <Routes>
          {/* Public Routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          {/* Protected Routes */}
          <Route element={<ProtectedRoute />}>
            <Route path="/" element={<Dashboard />} />
            <Route path="/configurations" element={<Configurations />} />
          </Route>
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

