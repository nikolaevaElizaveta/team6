from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

likes = {}  # dict for storing likes

MESSAGE_SERVICE_URL = 'http://localhost:5002'


@app.route('/like', methods=['POST'])
def like_message():
    message_id = request.json.get('message_id')
    key = str(message_id)

    response = requests.get(f'{MESSAGE_SERVICE_URL}/message_check', params={'message': message_id})
    # simple check if message exists

    if response.status_code != 200:
        return jsonify({'message': f'Message with id {message_id} not found!'}), 403

    if not likes.get(key):
        likes.setdefault(key, 1)
    else:
        likes[key] += 1
    return jsonify({'message': f'Message liked!'}), 201


@app.route('/likes', methods=['GET'])
def get_likes():
    message_id = request.args.get('message_id')
    return jsonify({'likes': likes.get(f"{message_id}", "Not found")}), 200


if __name__ == '__main__':
    app.run(port=5003)  # running service on port 5003
