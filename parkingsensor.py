from gpiozero import LED, Device, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

# NOTE: Change these numbers to match the GPIO pins you're connecting the LEDs and distance sensor to
sensor = DistanceSensor(echo=27, trigger=17)
red = LED(18)
yellow = LED(23)
green = LED(24)

# TODO: Turn off all lights after 15 seconds of no change

while True:
    distance = sensor.distance * 100

    if (distance < 50):
        red.on()
        green.off()
        yellow.off()
    elif (distance < 75):
        red.off()
        green.off()
        yellow.on()
    elif (distance < 100):
        green.on()
        red.off()
        yellow.off()
    else:
        red.off()
        yellow.off()
        green.off()
