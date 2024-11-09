from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/backend/compute-risk-score', methods=['POST'])
def add():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)
    result = x + y
    return jsonify({'result': result})


@app.route('/', methods=['POST'])
def multiply():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)
    result = x * y
    return jsonify({'result': result})



if __name__ == '__main__':
    app.run(debug=True)
