from flask import Flask, render_template, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons/<name>')
def person(name):
    filename = f'persons/{name}.html'
    path = os.path.join('templates', filename)
    if os.path.exists(path):
        return render_template(filename)
    else:
        abort(404)

if __name__ == '__main__':
    app.run()
