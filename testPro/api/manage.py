import os
import threading
import time
import requests
from flask import jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'dev'))
manager = Manager(app)
# migrate = Migrate(app, db)


@app.route('/hello')
def test():
    return "111111111111"



if __name__ == '__main__':
    manager.run()
