# Docker + local dev instructions

To start a local development environment with MySQL, backend, and frontend using Docker Compose:

1. Build and start services
   docker compose up --build

2. Seed the database (the backend service runs a seed script on startup if you run it manually).
   Or exec into the backend container and run:
   docker compose exec backend python seed.py

3. Visit frontend at http://localhost:5173 and backend at http://localhost:5000

Notes:
- The backend service reads environment variable DATABASE_URI to connect to the database. The docker-compose.yml provides a connection using the "db" service name.
- Uploaded resumes are stored in backend/uploads/resumes and are mounted into the container.
## Latest Update
## Latest Update
