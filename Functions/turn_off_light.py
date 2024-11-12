# Functions/turn_off_light.py
import RPi.GPIO as GPIO

def turn_off_light():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)  # Pin 18 for light control
    GPIO.output(18, GPIO.LOW)
    return "Light turned off."
