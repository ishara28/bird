import os
import redis
import flask
import json
import urlparse
from flask import Flask, Response, request, render_template
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
# redis_handle = redis.Redis(host=url.hostname, port=url.port, password=url.password)
redis_handle = redis.Redis('localhost')


@app.route('/')
@cross_origin()
def hello():
    return 'Hello World!'


@app.route('/users', methods=['GET'])
@cross_origin()
def get_user():
    response = {}
    user_id = request.args.get("id")
    user = redis_handle.get(user_id)
    if not user:
        response["msg"] = "no user found"
        return flask.jsonify(response)
    return user


@app.route('/clear', methods=['GET'])
@cross_origin()
def clear_data():
    redis_handle.flushall()
    return "ok!"


@app.route('/users', methods=['POST'])
@cross_origin()
def save_user():
    response = {}
    data = request.get_json(force=True)
    redis_handle.set(data["id"], json.dumps(data))
    response["status"] = "ok"
    return flask.jsonify(response)


@app.route('/users', methods=['DELETE'])
@cross_origin()
def delete_user():
    response = {}
    user_id = request.args.get("id")
    redis_handle.delete(user_id)
    response["status"] = "ok"
    return flask.jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
