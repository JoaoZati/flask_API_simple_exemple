from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_word():
    return 'Hello Word'


class Add(Resource):
    def post(self):
        # if i'm here, the resource add was requested using the method POST

        # Step 1: get the json data and manage errors
        try:
            post_data = request.get_json()

            x = float(post_data['x'])
            y = float(post_data['y'])
        except Exception as e:
            print(e)
            json_data = {
                'Message': f'ERROR: {e}',
                'Status Code': 301
            }
            return jsonify(json_data)

        # Step 3: do the calculation
        result = x + y

        # step 4: Create Json response and send
        json_data = {
            "Message": result,
            "Status Code": 200,
        }
        return jsonify(json_data)


class Subtract(Resource):
    pass


class Multiply(Resource):
    pass


class Divide(Resource):
    pass


api.add_resource(Add, "/add")


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
