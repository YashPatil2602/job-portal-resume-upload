from backend.app import create_app
from backend.database.db import db
from flask_migrate import Migrate, upgrade, migrate, revision
import sys

app = create_app()
migrate_obj = Migrate(app, db)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'upgrade'
    with app.app_context():
        if cmd == 'upgrade':
            upgrade()
        elif cmd == 'migrate':
            msg = sys.argv[2] if len(sys.argv) > 2 else 'autogenerate'
            migrate(message=msg)
        elif cmd == 'revision':
            msg = sys.argv[2] if len(sys.argv) > 2 else 'rev'
            revision(message=msg, autogenerate=True)
        else:
            print('Usage: manage.py [upgrade|migrate|revision]')
