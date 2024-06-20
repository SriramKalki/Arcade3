from app import create_app
from app.models import db
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app()
manager = Manager(app)

@manager.command
def run():
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()
