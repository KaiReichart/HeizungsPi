from app import app
import os, glob, time, serial

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

@app.route('/analogReading')
def analogReading():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    val = ""
    valList = []
    for _ in range(50):
        currReading = getReading(ser)
        if currReading is not None:
            valList.append(currReading)
    val = str( int( sum(valList) / len(valList) ) )
    return val

def getReading(ser):
    errorCounter = 0
    while True:
        if ser.in_waiting > 0:
            try:
                val = ser.readline().decode('utf-8').rstrip()
                return int(val)
            except:
                print("Error!")
                errorCounter += 1
                if errorCounter < 10:
                    return None

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
        temp_c = round(float(temp_string) / 1000.0, 1)
        return str(temp_c)
    return None

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

@app.route('/rolladenUp')
def rolladenUp():
    os.system('sudo python3 /home/pi/rolladen.py UP')
    return "OK"

@app.route('/rolladenDown')
def rolladenDown():
    os.system('sudo python3 /home/pi/rolladen.py DOWN')
    return "OK"