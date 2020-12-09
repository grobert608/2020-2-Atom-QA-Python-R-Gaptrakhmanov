import threading

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA = {}


# Напишем функцию, которая будет отвечать за запуск нашего приложения
def run_app(host, port):
    # Используем треды, чтобы была общая память с pytest

    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })

    server.start()
    return server


# Добавляем точку завершения приложения, чтобы мы могли его при необходимостм правильно закрыть
def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/auth')
def auth():
    if request.headers.get('Authorization'):
        mock_response = requests.get('http://127.0.0.1:5000/auth',
                                     headers={'Authorization': f'{request.headers["Authorization"]}'})
        if mock_response.status_code == 200:
            return jsonify("Success"), 200
        elif mock_response.status_code == 403:
            return jsonify("No user"), 403
        else:
            return jsonify("Not Success"), 400
    else:
        return jsonify("No headers"), 400


@app.route('/errorfzz')
def errorfzz():
    return requests.get('http://127.0.0.1:5000/errorfzz')


@app.route('/timeout')
def timeout():
    return requests.get('http://127.0.0.1:5000/timeout')


@app.route('/fake_mock')
def fake_mock():
    return requests.get('http://127.0.0.1:5003/fake_mock')


if __name__ == '__main__':
    run_app('127.0.0.1', 5001)
