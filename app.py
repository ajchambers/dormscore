from flask import Flask, render_template
import psycopg2
import psycopg2.extras

from fun import fetch_all_dorms, fetch_dorm_data, fetch_dorms_by_university

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/schools')
def schools():
    dorms_cmich = fetch_dorms_by_university('Central Michigan University')
    all_dorms = fetch_all_dorms()
    return render_template('schools.html', dorms_cmich=dorms_cmich, all_dorms=all_dorms)

@app.route('/dorm/<dorm_name>')
def dorm(dorm_name):
    dorm_template = fetch_dorm_data(dorm_name)
    return render_template(dorm_template)

if __name__ == '__main__':
    app.run(debug=True)
