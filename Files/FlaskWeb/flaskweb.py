import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    print("Receive Request from : " + str(request.environ.get('HTTP_X_Real_IP',request.remote_addr)))
    return "Hello DevC Members! You hit: " + socket.gethostname() + ". Version: 1.0"

if __name__ == '__main__':
    print("Web Server starting and listen to port 8080")
    # app.run(host="0.0.0.0", port= 8080, debug=True)
    app.run(host="0.0.0.0", port=8080)
