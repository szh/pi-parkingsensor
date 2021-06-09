# pi-parkingsensor
A simple Raspberry Pi project to assist with parking in a garage

Developed for the Pi Zero. Uses 3 LEDs - red, yellow, and green; and an ultrasonic distance sensor.

# Installing
On your Pi:
```
sudo apt-get update
sudo apt-get install python3-pip python-dev pigpio
sudo pip3 install gpiozero pigpio

nano /etc/rc.local
```
Now add the following text before `exit 0`:

```
pigpiod
python3 /home/pi/parkingsensor.py > /home/pi/log.txt &
```

Exit and reboot (`sudo reboot`).

Check out comments in the code for configuration options.
