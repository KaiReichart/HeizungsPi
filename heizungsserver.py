from app import app

try: 
    with open("/sys/class/gpio/export", "w") as f: 
        f.write("23")
except:
    print("Error Exporting GPIO PIN.")

try:
    with open("/sys/class/gpio/gpio23/direction", "w") as f:     
        f.write("out")
except:
    print("Error writing GPIO PIN direction.")
    