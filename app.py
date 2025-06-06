from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons/alishernavoiy')
def alishernavoiy():
    return render_template('persons/alishernavoiy.html')
