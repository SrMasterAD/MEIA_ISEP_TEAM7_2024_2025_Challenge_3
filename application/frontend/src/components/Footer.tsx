import { Github, Mail, Shield } from "lucide-react";

export default function Footer() {
  return (
    <footer className="bg-gradient-to-tr from-blue-50 via-white to-blue-100 border-t border-gray-200 py-8 px-4 text-sm text-gray-700">
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
        {/* Left */}
        <div className="flex text-center md:text-left space-y-1">
          <img
            src="/logo.png"
            alt="DeepWheat Logo"
            className="h-16 w-16 object-contain mr-2"
          />
          <div className="flex flex-col self-center">
            <p className="text-gray-500">AI-Powered Wheat Health Monitoring</p>
            <p className="text-xs text-gray-400">© {new Date().getFullYear()} All rights reserved.</p>
          </div>
        </div>

        {/* Right */}
        <div className="flex gap-6 items-center text-gray-600">
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1 hover:text-blue-600 transition"
          >
            <Github className="w-4 h-4" />
            GitHub
          </a>
          <a
            href="mailto:support@deepwheat.ai"
            className="flex items-center gap-1 hover:text-blue-600 transition"
          >
            <Mail className="w-4 h-4" />
            Contact
          </a>
          <a
            href="/privacy"
            className="flex items-center gap-1 hover:text-blue-600 transition"
          >
            <Shield className="w-4 h-4" />
            Privacy
          </a>
        </div>
      </div>
    </footer>
  );
}
