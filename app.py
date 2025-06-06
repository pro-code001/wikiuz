from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons/<person_name>')
def show_person(person_name):
    try:
        return render_template(f'persons/{person_name}.html')
    except:
        abort(404)  # Agar fayl topilmasa, 404 xatolik ko'rsatish
