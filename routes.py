from flask import jsonify, request, render_template
from app import app, db  # Import 'app' from 'app.py'
from models import Transaction
from ExchangeRate import ExchangeRate

exchange = ExchangeRate()

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    result = []
    for transaction in transactions:
        result.append({
            'id': transaction.id,
            'amount': transaction.amount,
            'spent': transaction.spent,
            'created_at': transaction.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result)

@app.route('/balance', methods=['GET'])
def get_balance():
    transactions = Transaction.query.all()
    unspent_transactions = [transaction for transaction in transactions if not transaction.spent]
    btc_balance = sum([transaction.amount for transaction in unspent_transactions])
    eur_balance = exchange.btc_to_eur(btc_balance)
    return jsonify({'BTC': btc_balance, 'EUR': eur_balance})

@app.route('/transfer', methods=['POST'])
def create_transfer():
    data = request.json
    transfer_amount_eur = data.get('amount')

    exchange_rate = exchange.get_exchange_rate()
    transfer_amount_btc = transfer_amount_eur / exchange_rate

    transactions = Transaction.query.all()
    unspent_transactions = [transaction for transaction in transactions if not transaction.spent]
    total_btc_available = sum([transaction.amount for transaction in unspent_transactions])

    if transfer_amount_btc > total_btc_available or transfer_amount_btc < 0.00001:
        return jsonify({'error': 'Insufficient balance or transfer amount too small'}), 400

    # Deduct the transfer amount from unspent transactions
    transferred_amount = 0
    for transaction in unspent_transactions:
        if transferred_amount >= transfer_amount_btc:
            break
        transaction.spent = True
        transferred_amount += transaction.amount

    # Calculate leftover amount
    leftover_btc = transferred_amount - transfer_amount_btc
    if leftover_btc > 0:
        leftover_transaction = Transaction(amount=leftover_btc)
        db.session.add(leftover_transaction)

    db.session.commit()

    return jsonify({'message': 'Transfer successful'}), 200

@app.route('/')
def index():
    # Fetch all transactions
    transactions = Transaction.query.all()

    # Calculate wallet balance
    unspent_transactions = [transaction for transaction in transactions if not transaction.spent]
    btc_balance = sum([transaction.amount for transaction in unspent_transactions])
    eur_balance = exchange.btc_to_eur(btc_balance)

    # Render the template with transactions and balance
    return render_template('Page.html', transactions=transactions, btc_balance=btc_balance, eur_balance=eur_balance)

