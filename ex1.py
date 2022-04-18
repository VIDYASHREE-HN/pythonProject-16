# import RPi.GPIO as GPIO
import pigpio
import time

gpio_pin = 17
_pi = pigpio.pi()

while(1):
    _pi.write(gpio_pin,1)
    # a = _pi.read(gpio_pin)
    time.sleep(1)
    _pi.write(gpio_pin, 0)
    #b = _pi.write(gpio_pin,0)
    time.sleep(1)
    # print(a)



# gpio.setmode(gpio.BOARD)
#
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(27, GPIO.OUT)
# GPIO.setup(22, GPIO.OUT)
#
# GPIO.setup(17, GPIO.HIGH)
# time.sleep(.5)
# GPIO.setup(17, GPIO.LOW)
#
# GPIO.setup(27, GPIO.HIGH)
# time.sleep(.5)
# GPIO.setup(27, GPIO.LOW)
#
#
# GPIO.setup(22, GPIO.HIGH)
# time.sleep(.5)
# GPIO.setup(22, GPIO.LOW)
#
#
# GPIO.cleanup()

