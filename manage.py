from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from apps import get_app

app = get_app()

manager = Manager(app)

manager.add_command('start', Server(host='127.0.0.1', port=2333))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()