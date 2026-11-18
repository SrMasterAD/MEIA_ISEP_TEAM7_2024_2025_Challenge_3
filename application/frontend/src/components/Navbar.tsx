import { Link, useNavigate } from "react-router-dom";
import { LogOut, Settings, FileBarChart } from "lucide-react";

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login")
  };

  return (
    <nav className="bg-white border-b border-gray-200 shadow-sm px-2 py-1 flex items-center justify-between">
      {/* Logo + Brand Name */}
      <Link to="/" className="flex items-center gap-3">
        <img
          src="/logo.png"
          alt="DeepWheat Logo"
          className="h-16 w-16 object-contain"
        />
      </Link>

      {/* Navigation Links */}
      <ul className="flex items-center gap-6 text-gray-700 font-medium text-sm">
        <li>
          <Link
            to="/"
            className="group relative transition"
          >
            <span className="flex items-center gap-1 hover:text-blue-600 transition">
              <FileBarChart size={16} />
              Reports
            </span>
            <span className="absolute left-0 bottom-0 w-0 h-0.5 bg-blue-600 transition-all group-hover:w-full"></span>
          </Link>
        </li>
        <li>
          <Link
            to="/configurations"
            className="group relative transition"
          >
            <span className="flex items-center gap-1 hover:text-blue-600 transition">
              <Settings size={16} />
              Configurations
            </span>
            <span className="absolute left-0 bottom-0 w-0 h-0.5 bg-blue-600 transition-all group-hover:w-full"></span>
          </Link>
        </li>
        <li>
          <button
            onClick={handleLogout}
            className="flex items-center gap-1 bg-red-100 text-red-600 px-3 py-1.5 rounded-xl hover:bg-red-200 transition text-sm"
          >
            <LogOut size={16} />
            Logout
          </button>
        </li>
      </ul>
    </nav>
  );
}
