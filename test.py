from flask import Flask, jsonify, request
import time

app = Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    params = request.get_json()
    try:
        name = params['name'];
        age = int(params['age']);
    except:
        return jsonify({'error': 'missing parameter'})
    return jsonify({"your name:": name, "your age:": age, "response": 'sample response'})


if __name__ == '__main__':
    app.run(debug=False)
