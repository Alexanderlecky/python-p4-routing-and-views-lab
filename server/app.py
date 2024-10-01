#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Base route to display the title of the app
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string in the console and display it in the browser
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    if parameter < 0:
        return "Invalid input, parameter should be a non-negative integer", 400
    count_str = '\n'.join(str(i) for i in range(parameter))
    # Returning plain text with newlines
    return count_str + '\n'


# Route to perform basic math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        # Adding a status code for invalid operations
        return "Invalid operation", 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
