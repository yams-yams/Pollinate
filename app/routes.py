from app import app
from flask import Flask
from flask import url_for
from flask import render_template
from markupsafe import escape



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'yamsyams'}
    elections = [
        {
            'question': 'Ketchup or Mustard?',
            'choice1': 'Ketchup',
            'choice2': 'Mustard',
        },
        {
            'question': 'Sweet or Sour?',
            'choice1': 'Sweet',
            'choice2': 'Sour',
        },
        {
            'question': 'Green or Blue?',
            'choice1': 'Sweet',
            'choice2': 'Sour',
        },
    ]
    return render_template('index.html', user=user, elections=elections)

@app.route('/<name>')
def hello_name(name):
    return f'Hello {escape(name)}'
