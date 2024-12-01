from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f'<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f/<celsius>')
def f(celsius=""):
    return f"{celsius} degrees Celcius = {convert_celsius_to_fahrenheit(celsius)} Fahrenheit"

def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit

if __name__ == '__main__':
    app.run()
