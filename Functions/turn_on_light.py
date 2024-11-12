# Functions/turn_on_light.py
import RPi.GPIO as GPIO

def turn_on_light():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)  # Pin 18 for light control
    GPIO.output(18, GPIO.HIGH)
    return "Light turned on."
