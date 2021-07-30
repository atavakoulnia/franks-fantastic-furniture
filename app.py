from flask import Flask, render_template, url_for
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

# Listener

if __name__ == "__main__":
    app.run(debug=True)