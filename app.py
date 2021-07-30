from flask import Flask, render_template, url_for

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def index():
    return render_template('index.html')

# Listener

if __name__ == "__main__":
    app.run(debug=True)