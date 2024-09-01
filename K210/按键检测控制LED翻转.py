import utime
from fpioa_manager import fm
from Maix import GPIO

io_led_green = 12
io_led_red   = 13
io_led_blue  = 14

io_boot_key  = 16

fm.register(io_led_green, fm.fpioa.GPIO0)
fm.register(io_led_red, fm.fpioa.GPIO1)
fm.register(io_led_blue, fm.fpioa.GPIO2)

fm.register(io_boot_key, fm.fpioa.GPIO3)

led_g=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r=GPIO(GPIO.GPIO1, GPIO.OUT)
led_b=GPIO(GPIO.GPIO2, GPIO.OUT)

key  =GPIO(GPIO.GPIO3, GPIO.IN)

led_g.value(1)
led_r.value(1)
led_b.value(1)

led_State = True

while True:
    if key.value() == 0:
        utime.sleep_ms(20)
        if key.value() == 0:
            led_State = not led_State
            led_b.value(led_State)
        while(key.value() == 0):
            utime.sleep_ms(20)



