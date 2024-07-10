#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<string:text>")
def user(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def counter(number):
    count = ''
    for (i) in range(number):
        count += f'{i}\n'
    return count

@app.route('/math/<int:a>/<operation>/<int:b>')
def mathOperations(a, operation, b):
    if operation == '+':
        return str(a + b)
    elif operation == '-':
        return str(a - b)
    elif operation == '*':
        return str(a * b)
    elif operation == 'div':
        return str(a / b)
    elif operation == '%':
        return str(a % b)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
