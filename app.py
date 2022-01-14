from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello Word'


@app.route('/hithere')
def hi_there():
    return 'Hi there'


@app.route('/calc')
def calc():
    # prepare a response
    c = 200 * 3.14
    return f'{str(c)}'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
