from flask import Flask, request, jsonify

app = Flask(__name__)

likes = {}  # Словарь для хранения лайков сообщений

@app.route('/like', methods=['POST'])
def like_message():
    message_id = request.json.get('message_id')
    if message_id not in likes:
        likes[message_id] = 0
    likes[message_id] += 1
    return jsonify({'message': 'Message liked!'}), 201

@app.route('/likes', methods=['GET'])
def get_likes():
    message_id = request.args.get('message_id')
    return jsonify({'likes': likes.get(message_id, 0)}), 200

if __name__ == '__main__':
    app.run(port=5003)  # Запускаем сервис на порту 5003
