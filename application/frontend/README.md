# Frontend Application - DeepWheat

This is the frontend application for the DeepWheat project, an AI-powered wheat health monitoring system.

## Prerequisites

Before running the application, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (version 18 or higher recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd application/frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

## Running the Application

To start the development server:

```bash
npm run dev
```

This will start the application on `http://localhost:5173` by default. Open your browser and navigate to this URL to view the application.

## Linting

To lint the codebase and ensure code quality:

```bash
npm run lint
```

## Configuration

The application uses the following configuration files:

- `vite.config.ts`: Vite configuration
- `tailwind.config.js`: Tailwind CSS configuration
- `.prettierrc`: Prettier configuration
- `tsconfig.json`: TypeScript configuration

## Project Structure

The project is organized as follows:

```
src/
├── components/       # Reusable React components
├── lib/              # Utility libraries (e.g., API client)
├── models/           # TypeScript models
├── pages/            # Page components for routing
├── security/         # Security-related components (e.g., ProtectedRoute)
├── assets/           # Static assets
├── App.tsx           # Main application component
├── main.tsx          # Application entry point
```

## API Integration

The application communicates with the backend API hosted at `http://localhost:8000`. Ensure the backend server is running before using the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
