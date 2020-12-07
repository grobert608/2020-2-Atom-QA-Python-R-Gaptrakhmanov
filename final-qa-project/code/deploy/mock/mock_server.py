import threading

from flask import Flask, abort, request, jsonify, make_response

app = Flask(__name__)
users = {'robert': 1}


def run_mock(host, port):
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.vk_client.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/vk_id/<username>')
def get_user_by_username(username: str):
    vk_id = users.get(str(username), None)
    if vk_id:
        data = {'vk_id': vk_id}
        return make_response(jsonify(data), 200)
    else:
        return abort(404)


@app.route('/get_all')
def get_all():
    return make_response(jsonify(users), 200)


@app.route('/add', methods=['POST'])
def post_user():
    username = str(request.get_data()).split('&')[0].split('=')[1]
    vk_id = str(request.get_data()).split('&')[1].split('=')[1]
    users[username] = vk_id
    return make_response('', 201)


@app.route('/del_user/<username>')
def del_user(username):
    user_id = users.get(str(username), None)
    if user_id:
        users.pop(username)
        return make_response('', 204)
    else:
        return abort(400)


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock('0.0.0.0', 5000)
