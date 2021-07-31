from flask import Flask, render_template, url_for, request
import database.db_connector as db
# ---------------------------------------------------------------------------------------
#                                   Configuration
# ---------------------------------------------------------------------------------------
app = Flask(__name__)
db_connection = db.connect_to_database()
# ---------------------------------------------------------------------------------------
#                                       Routes 
# ---------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers', methods=['POST', 'GET'])
def customers():
    query = "SELECT * FROM customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('customers.html', customers=results)

@app.route('/orders', methods=['POST', 'GET'])
def orders():
    query = "SELECT * FROM orders;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('orders.html', orders=results)

@app.route('/transactions', methods=['POST', 'GET'])
def transactions():
    query = "SELECT * FROM transactions;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('transactions.html', transactions=results)

@app.route('/products', methods=['POST', 'GET'])
def products():
    query = "SELECT * FROM products;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('products.html', products=results)

@app.route('/employees', methods=['POST', 'GET'])
def employees():
    query = "SELECT * FROM employees;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('employees.html', employees=results)
# ---------------------------------------------------------------------------------------
@app.route('/form', methods=['POST'])
def form():
    title = "Thank you, attributes have been successfully added! (not really though)"
    return render_template('form.html', title=title)
# ---------------------------------------------------------------------------------------
#                                       Listener
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
