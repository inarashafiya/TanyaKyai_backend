from app import app,create_app, db
from flask_migrate import Migrate
from os import getenv

apps = create_app(app)
Migrate(apps, db)

host = getenv('FLASK_RUN_HOST')
port = getenv('FLASK_RUN_PORT')

print(port)

if __name__ == '__main__':
    app.run(host=host, debug=True, port=port)
