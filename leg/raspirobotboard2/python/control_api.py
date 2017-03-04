from flask import Flask
from controller import controller
app = Flask(__name__)

motor = controller()

@app.route("/")
def index():
    return "motor controller"

@app.route("/forward")
def forward():
    motor.forward()
    return "forward"


@app.route("/reverse")
def reverse():
    motor.reverse()
    return "reverse"

@app.route("/left")
def left():
    motor.left()
    return "left"

@app.route("/right")
def right():
    motor.right()
    return "right"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)