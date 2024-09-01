from machine import Timer
from machine import PWM
import time
import utime

io_servo_pin = 22

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode = Timer.MODE_PWM)

S1 = PWM(tim, freq = 50, duty = 0, pin = io_servo_pin)

def Servo(angle):
    S1.duty(angle/180*10+2.5)

while(1):

    for i in range(0, 90, 1):
        Servo(i)
        utime.sleep_ms(20)
    utime.sleep_ms(2000)

    for i in range(90, 0, -1):
        Servo(i)
        utime.sleep_ms(20)

    break
