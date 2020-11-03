from app import app
import os, glob, time

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

@app.route('/temperature')
def temperature():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return str(temp_c)
    return None

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines