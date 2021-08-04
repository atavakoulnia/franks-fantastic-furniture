from flask import Flask, render_template, url_for, request, redirect, flash
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
@app.route('/delete_customers/<int:id>', methods=['POST', 'GET'])
def delete_customers(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        query = 'DELETE FROM customers WHERE customer_id = %s'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect(url_for('customers'))
    else:
        return redirect(url_for('customers'))
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
    customer_id = request.form['customer_id']
    query = 'INSERT INTO orders (customer_id) VALUES (%s)'
    data = (customer_id)
    db.execute_query(db_connection, query, data)
    return redirect(url_for('orders'))
# ------------------------------UPDATE for Orders Page-----------------------------------
@app.route('/update_orders/<int:order_id>', methods=['POST','GET'])
def update_orders(order_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Orders Page-----------------------------------
@app.route('/delete_orders/<int:id>', methods=['POST', 'GET'])
def delete_orders(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        query = 'DELETE FROM orders WHERE order_id = %s'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect(url_for('orders'))
    else:
        return redirect(url_for('orders'))
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
@app.route('/delete_transactions/<int:id>', methods=['POST', 'GET'])
def delete_transactions(id):
    db_connection = db.connect_to_database()
    query = 'DELETE FROM transactions WHERE transaction_id = %s'
    data = (id,)
    result = db.execute_query(db_connection, query, data)
    return redirect(url_for('transactions'))
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
    product_name = request.form['product_name']
    unit_price = request.form['unit_price']
    query = 'INSERT INTO products (product_name, unit_price) VALUES (%s,%s)'
    data = (product_name, unit_price)
    db.execute_query(db_connection, query, data)
    return redirect(url_for('products'))
# ------------------------------UPDATE for Products Page---------------------------------
@app.route('/update_products/<int:product_id>', methods=['POST','GET'])
def update_products(product_id):
    db_connection = db.connect_to_database()
    pass
# ------------------------------DELETE for Products Page---------------------------------
@app.route('/delete_products/<int:id>', methods=['POST', 'GET'])
def delete_products(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        query = 'DELETE FROM products WHERE product_id = %s'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect(url_for('products'))
    else:
        return redirect(url_for('products'))
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
@app.route('/delete_employees/<int:id>', methods=['POST', 'GET'])
def delete_employees(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        query = 'DELETE FROM employees WHERE employee_id = %s'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect(url_for('employees'))
    else:
        return redirect(url_for('employees'))
# ---------------------------------------------------------------------------------------
#                                       Listener
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(port=port, debug=True)
