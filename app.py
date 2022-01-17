from flask import Flask, jsonify, request

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


@app.route('/json')
def simple_json():
    json_ex = {
        'Name': 'joao',
        'Age': 27,
        "phones": [
            {
                'phone_name': 'Xaiomi',
                'phone_number': 11111
            },
            {
                'phone_name': 'Iphone',
                'phone_number': 22222
            },
        ]
    }
    return jsonify(json_ex)


@app.route('/add_two_numbers', methods=["POST"])
def add_two_numbers():
    data = request.get_json()

    try:
        x = float(data['x'])
        y = float(data['y'])
    except Exception as e:
        print(e)
        return "ERROR", 305

    z = x + y

    json_data = {
        "z": z
    }
    return jsonify(json_data), 200


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
