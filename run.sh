echo "23" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio23/direction

export FLASK_APP=heizungsserver.py
python3 -m flask run --host=0.0.0.0