from flask import Flask, render_template
from flask_cors import CORS

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    app.run()
