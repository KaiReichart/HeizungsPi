from app import app

with open("/sys/class/gpio/export", "w") as f: 
    f.write("23")

with open("/sys/class/gpio/gpio23/direction", "w") as f: 
    f.write("out")