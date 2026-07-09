# Alembic and migrations

To generate or run migrations locally:

1. Activate your backend virtualenv and install dev requirements:
   pip install -r backend/requirements-dev.txt

2. Initialize migrations (only once if not present):
   cd backend
   flask db init

   Note: the repository already contains a migrations/ folder with an initial migration.

3. To apply migrations:
   python backend/manage.py upgrade

4. To create a new migration (after changing models):
   python backend/manage.py migrate "message"
   python backend/manage.py upgrade

If you use Docker Compose, you can run the upgrade inside the backend container:

  docker compose exec backend python manage.py upgrade
