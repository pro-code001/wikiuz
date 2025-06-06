from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons/<person_name>')
def person_page(person_name):
    try:
        return render_template(f'persons/{person_name}.html')
    except:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
