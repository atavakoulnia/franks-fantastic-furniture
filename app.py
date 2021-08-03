from flask import Flask, render_template, url_for, request, redirect
import os
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
# ---------------------------------------------------------------------------------------
#                                   Customers Page 
# ---------------------------------------------------------------------------------------
# ------------------------------READ for Customers Page----------------------------------
@app.route('/customers', methods=['POST', 'GET'])
def customers():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('customers.html', customers=results)
# ------------------------------CREATE for Customers Page--------------------------------
@app.route('/add_customers', methods=['POST'])
def add_customers():
    db_connection = db.connect_to_database()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    phone_number = request.form['phone_number']
    query = 'INSERT INTO customers (first_name, last_name, address, phone_number) VALUES (%s,%s,%s,%s)'
    data = (first_name, last_name, address, phone_number)
    db.execute_query(db_connection, query, data)
    return redirect(url_for('customers'))
# ------------------------------UPDATE for Customers Page--------------------------------
@app.route('/update_customers/<int:customer_id>', methods=['POST','GET'])
def update_customers(customer_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Customers Page--------------------------------
@app.route('/delete_customers/<int:customer_id>')
def delete_customers(customer_id):
    db_connection = db.connect_to_database()
    pass
# ---------------------------------------------------------------------------------------
#                                   Orders Page 
# ---------------------------------------------------------------------------------------
# ------------------------------READ for Orders Page-------------------------------------
@app.route('/orders', methods=['POST', 'GET'])
def orders():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM orders;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('orders.html', orders=results)
# ------------------------------CREATE for Orders Page-----------------------------------
@app.route('/add_orders', methods=['POST'])
def add_orders():
    db_connection = db.connect_to_database()
    pass
# ------------------------------UPDATE for Orders Page-----------------------------------
@app.route('/update_orders/<int:order_id>', methods=['POST','GET'])
def update_orders(order_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Orders Page-----------------------------------
@app.route('/delete_orders/<int:order_id>')
def delete_orders(order_id):
    db_connection = db.connect_to_database()
    pass
# ---------------------------------------------------------------------------------------
#                                   Transactions Page 
# ---------------------------------------------------------------------------------------
# ------------------------------READ for Transactions Page-------------------------------
@app.route('/transactions', methods=['POST', 'GET'])
def transactions():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM transactions;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('transactions.html', transactions=results)
# ------------------------------CREATE for Transactions Page-----------------------------
@app.route('/add_transactions', methods=['POST'])
def add_transactions():
    db_connection = db.connect_to_database()
    pass
# ------------------------------UPDATE for Transactions Page-----------------------------
@app.route('/update_transactions/<int:transaction_id>', methods=['POST','GET'])
def update_transactions(transaction_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Transactions Page-----------------------------
@app.route('/delete_transactions/<int:transactions_id>')
def delete_transactions(transaction_id):
    db_connection = db.connect_to_database()
    pass
# ---------------------------------------------------------------------------------------
#                                   Products Page 
# ---------------------------------------------------------------------------------------
# ------------------------------READ for Products Page-----------------------------------
@app.route('/products', methods=['POST', 'GET'])
def products():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM products;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('products.html', products=results)
# ------------------------------CREATE for Products Page---------------------------------
@app.route('/add_products', methods=['POST'])
def add_products():
    db_connection = db.connect_to_database()
    pass
# ------------------------------UPDATE for Products Page---------------------------------
@app.route('/update_products/<int:product_id>', methods=['POST','GET'])
def update_products(product_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Products Page---------------------------------
@app.route('/delete_products/<int:product_id>')
def delete_products(product_id):
    db_connection = db.connect_to_database()
    pass
# ---------------------------------------------------------------------------------------
#                                   Employees Page 
# ---------------------------------------------------------------------------------------
# ------------------------------READ for Employees Page----------------------------------
@app.route('/employees', methods=['POST', 'GET'])
def employees():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM employees;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template('employees.html', employees=results)
# ------------------------------CREATE for Employees Page--------------------------------
@app.route('/add_employees', methods=['POST'])
def add_employees():
    db_connection = db.connect_to_database()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    query = 'INSERT INTO employees (first_name, last_name) VALUES (%s,%s)'
    data = (first_name, last_name)
    db.execute_query(db_connection, query, data)
    return redirect(url_for('employees'))
# ------------------------------UPDATE for Employees Page--------------------------------
@app.route('/update_employees/<int:employee_id>', methods=['POST','GET'])
def update_employees(employee_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Employees Page--------------------------------
@app.route('/delete_employees/<int:employee_id>')
def delete_employees(employee_id):
    db_connection = db.connect_to_database()
    pass
# ---------------------------------------------------------------------------------------
#                                       Listener
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(port=port, debug=True)