import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../lib/api";
import { Toast } from "primereact/toast";
import { AuthResponse } from "../models/auth-response.model";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const toast = useRef<Toast>(null);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await api.post<AuthResponse>("/login", { email, password });
      localStorage.setItem("token", response.data.access_token);
      navigate("/");
    } catch (err: any) {
      const errorMsg = err.response?.data?.message || "Login failed";
      toast.current?.show({
        severity: "error",
        summary: "Login Error",
        detail: errorMsg,
        life: 4000,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-12 flex items-center justify-center px-4">
      <Toast ref={toast} />
      <form
        onSubmit={handleLogin}
        className="bg-white p-8 rounded-2xl shadow-md w-full max-w-md space-y-6"
      >
        <h2 className="text-2xl font-bold text-center text-gray-800">Login</h2>

        <div>
          <label className="block text-sm font-medium text-gray-600 mb-1">
            Email
          </label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-600 mb-1">
            Password
          </label>
          <input
            type="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-xl transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? "Signing In..." : "Sign In"}
        </button>

        <div className="mt-4 text-center text-sm text-gray-600">
          Don’t have an account?{" "}
          <span
            className="text-blue-600 hover:underline cursor-pointer font-medium"
            onClick={() => navigate("/register")}
          >
            Click here
          </span>{" "}
          to register.
        </div>
      </form>
    </div>
  );
}
