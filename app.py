from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from ExchangeRate import ExchangeRate


app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
db = SQLAlchemy(app)

from routes import *

#main class
class MainApp:
    # constructor
    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.exchange_rate = ExchangeRate()

    def run(self):
        self.app.run(debug=False)


main_app = MainApp(app, db)

#run application, for me it gave running on http://127.0.0.1:5000
if __name__ == '__main__':
    main_app.run()
