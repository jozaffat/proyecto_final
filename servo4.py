import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led=18
#configura al pin gpio18 como salida
GPIO.setup(led, GPIO.OUT)   
p = GPIO.PWM(led, 50)  
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.5)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()