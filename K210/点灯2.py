#引入需要用到的硬件库
import utime
from Maix import GPIO
from fpioa_manager import fm

io_led_g = 12
io_led_r = 13
io_led_b = 14

#注册gpio外设资源到某个具体引脚
fm.register(io_led_g,fm.fpioa.GPIO0)
fm.register(io_led_r,fm.fpioa.GPIO1)
fm.register(io_led_b,fm.fpioa.GPIO2)


#申请定义一个GPIO对象，并设置工作模式
io_led_g = GPIO(GPIO.GPIO0,GPIO.OUT)
io_led_r = GPIO(GPIO.GPIO1,GPIO.OUT)
io_led_b = GPIO(GPIO.GPIO2,GPIO.OUT)

while(1):

    io_led_g.value(0)
    io_led_r.value(0)
    io_led_b.value(0)
    utime.sleep_ms(500)
    io_led_g.value(1)
    io_led_r.value(1)
    io_led_b.value(1)
    utime.sleep_ms(500)

unregister(io_led_g)
unregister(io_led_r)
unregister(io_led_b)
