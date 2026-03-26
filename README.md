# Brevooo - FastAPI AI-Powered application

Brevooo is a modern, modular FastAPI project designed to be a robust foundation for building AI-driven applications. It follows a clean architecture pattern, separating concerns into routers, services, schemas, and core logic.

## 🚀 Features

- **Modular Architecture**: Organized into logical components for easy scalability and maintenance.
- **FastAPI**: High-performance web framework for building APIs with Python 3.12+.
- **Poetry**: Dependency management and packaging made easy.
- **Pydantic V2**: Modern data validation and settings management.
- **AI Core**: Dedicated space for integrating AI models and processing logic.
- **Automatic Docs**: Interactive API documentation with Swagger UI and ReDoc.

---

## 📂 Project Structure

The project follows a structured layout to keep the codebase clean and manageable:

```text
app/
 ├── main.py                # Entry point: Initializes FastAPI and includes routers.
 ├── routers/               # API Endpoints: Defines the routes and handles requests.
 │    └── example_router.py
 ├── services/              # Business Logic: Contains the core logic of the application.
 │    └── example_service.py
 ├── core/                  # Core Modules: Shared logic, AI processors, and utilities.
 │    └── ai.py
 ├── schemas/               # Data Transfer Objects: Pydantic models for validation.
 │    └── example_schema.py
 ├── config/                # Configuration: Manages environment variables and settings.
 │    └── settings.py
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Brevooo
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. (Optional) Create a `.env` file in the root directory for your environment variables.

### Running the Application

Start the development server with hot-reload enabled:

```bash
poetry run uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation for your API:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Test your endpoints directly from the browser.
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) - Clean and professional API documentation.

---

## 🧪 Testing

Run tests using `pytest` (once implemented):

```bash
poetry run pytest
```

---

## 🤝 Contribution

Feel free to open issues or submit pull requests to improve the project!
