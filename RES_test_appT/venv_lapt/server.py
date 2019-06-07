from flask import Flask
from flask import request
import json

app = Flask(__name__)
get_msg = ""
msg = ""


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/secret')
def hello_secret():
    return "Hidden message."


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/get', methods=['GET'])
def get_handler():
    return 'Basic GET handler.'


@app.route('/get/<name>', methods=['GET'])
def get_name(name):
    global get_msg
    get_msg = name
    return 'GET handler. Hello {}!'.format(name)


@app.route('/put/json', methods=['PUT'])
def put_handler():
    json_obj = json.loads(request.data)
    print("JSON PUT handler. Received data:")
    print("Name: " + json_obj["name"] + ", job: " + json_obj["job"])
    return 'PUT handler.' + ' ' + json_obj["name"]


@app.route('/post', methods=['POST'])
def post_handler():
    global get_msg
    return str(get_msg)


@app.route('/post/json', methods=['POST'])
def json_post_handler():
    return 'JSON POST handler'


@app.route('/<welcome>', methods=['POST', 'PUT'])
def url_welcome(welcome):
    global msg
    txt = request.args.get('text')
    msg = welcome
    return txt + " " + msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
