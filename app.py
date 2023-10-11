from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')
