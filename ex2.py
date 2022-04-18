import pigpio
import time
pi = pigpio.pi()
pi.set_mode(5, pigpio.OUTPUT)
while (True):
    pi.write(5, True)
    time.sleep(0.5)
    pi.write(5, False)
    time.sleep(0.5)