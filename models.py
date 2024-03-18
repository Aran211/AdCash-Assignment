import datetime
import random
import string
from app import db
#I inserted test data to the database using this:
#INSERT INTO transaction (id, amount, spent, created_at)
#SELECT
#    md5(random()::text || clock_timestamp()::text)::varchar(64) AS id,
#    random() * 10 AS amount,
#    FALSE AS spent,
#    now() - random() * interval '365 days' AS created_at
#FROM
#    generate_series(1, 1000);
#Transaction model with id, amount, spent, created_at to database
class Transaction(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    amount = db.Column(db.Float)
    spent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    #constructor
    def __init__(self, amount):
        self.id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self.amount = amount
        self.spent = False

    #string representation of the object
    def __repr__(self):
        return f'<Transaction {self.id}>'