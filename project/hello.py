import time

from flask import Flask, request

application = Flask(__name__)


@application.route("/")
def route():
    time_to_sleep = request.args.get('sleep', 0)
    time.sleep(int(time_to_sleep))
    return f"<h1 style='color:blue'>Hello There! Sleep for {time_to_sleep} secs</h1>"


@application.route("/hello")
def hello():
    time_to_sleep = request.args.get('sleep', 0)
    time.sleep(int(time_to_sleep))
    return f"<h1 style='color:blue'>Hello from \hello! Sleep for {time_to_sleep} secs</h1>"


if __name__ == "__main__":
    application.run(host='0.0.0.0')
