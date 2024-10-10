from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

messages = []  # list for storing messages

USER_SERVICE_URL = 'http://localhost:5001'  # URL User Service


@app.route('/post', methods=['POST'])
def post_message():
    username = request.json.get('username')
    message = request.json.get('message')

    if len(message) > 400:
        return jsonify({'message': 'Message is too long!'}), 400

    # check if user is registered
    response = requests.get(f'{USER_SERVICE_URL}/check', params={'username': username})
    if response.status_code != 200:
        return jsonify({'message': 'User is not registered!'}), 403

    messages.append({'username': username, 'message': message})
    return jsonify({'message': f'Message {len(messages) - 1} posted!'}), 201


@app.route('/feed', methods=['GET'])
def get_feed():
    # returning last 10 messages
    return jsonify(messages[-10:]), 200


@app.route('/message_check', methods=['GET'])
def check_message():  # message existence checker, just via try catch on index
    message = int(request.args.get('message'))
    try:
        return jsonify({'Message': f"{messages[message]}"}), 200
    except IndexError:
        return jsonify({'Message': 'Message not found'}), 404


if __name__ == '__main__':
    app.run(port=5002)  # running service on port 5002
