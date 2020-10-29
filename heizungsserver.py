from app import app

with open("/sys/class/gpio/export", "w") as f: 
    try:
        f.write("23")
    except:
        print("Error Exporting GPIO PIN.")

with open("/sys/class/gpio/gpio23/direction", "w") as f: 
    try:
        f.write("out")
    except:
        print("Error writing GPIO PIN direction.")
    