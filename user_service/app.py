from flask import Flask, request, jsonify

app = Flask(__name__)

users = set()  # set for storing users


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    if username in users:
        return jsonify({'message': 'Username already exists!'}), 400
    users.add(username)
    return jsonify({'message': 'User registered!'}), 201


@app.route('/check', methods=['GET'])
def check():
    username = request.args.get('username')
    if username in users:
        return jsonify({'registered': True}), 200
    return jsonify({'registered': False}), 404


if __name__ == '__main__':
    app.run(port=5001)  # running service on port 5001
