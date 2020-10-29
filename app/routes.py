from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/on')
def turnOn():
    with open("/sys/class/gpio/gpio23/value", "w") as f: 
        f.write("1")
    return "OK"

@app.route('/off')
def turnOff():
    with open("/sys/class/gpio/gpio23/value", "w") as f: 
        f.write("0")
    return "OK"

@app.route('/status')
def status():
    with open("/sys/class/gpio/gpio23/value", "r") as f: 
        val = f.read()
    return val