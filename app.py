from flask import Flask, render_template, url_for, request
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers', methods=['POST', 'GET'])
def customers():
    query = "SELECT * FROM customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('customers.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/employees')
def employees():
    return render_template('employees.html')

# Listener

if __name__ == "__main__":
    app.run(debug=True)