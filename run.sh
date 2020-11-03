if [ -n "$1" ]; then
    echo "Running in Temp Sensor mode!"
else
    echo "23" > /sys/class/gpio/export || TRUE
    echo "out" > /sys/class/gpio/gpio23/direction || TRUE
fi


export FLASK_APP=heizungsserver.py
python3 -m flask run --host=0.0.0.0