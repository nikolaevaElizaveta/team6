from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

messages = []  # Список для хранения сообщений

USER_SERVICE_URL = 'http://localhost:5001'  # URL User Service

@app.route('/post', methods=['POST'])
def post_message():
    username = request.json.get('username')
    message = request.json.get('message')

    if len(message) > 400:
        return jsonify({'message': 'Message is too long!'}), 400

    # Проверяем, зарегистрирован ли пользователь
    response = requests.get(f'{USER_SERVICE_URL}/check', params={'username': username})
    if response.status_code != 200:
        return jsonify({'message': 'User is not registered!'}), 403

    messages.append({'username': username, 'message': message})
    return jsonify({'message': 'Message posted!'}), 201

@app.route('/feed', methods=['GET'])
def get_feed():
    # Возвращаем последние 10 сообщений
    return jsonify(messages[-10:]), 200

if __name__ == '__main__':
    app.run(port=5002)  # Запускаем сервис на порту 5002
