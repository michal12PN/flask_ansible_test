import socket
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! + {0}</h1>".format(socket.gethostname())

if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8000)
