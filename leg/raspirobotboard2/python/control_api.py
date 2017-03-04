from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "motor controller"

@app.route("/forward")
def forward():
    return "forward"


@app.route("/reverse")
def reverse():
    return "reverse"

@app.route("/left")
def left():
    return "left"

@app.route("/right")
def right():
    return "right"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)