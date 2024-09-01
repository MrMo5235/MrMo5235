#引入硬件库
from machine import UART
from fpioa_manager import fm

#串口资源注册
fm.register(24, fm.fpioa.UART1_TX, force = True)
fm.register(25, fm.fpioa.UART1_RX, force = True)

#初始化串口对象
uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout = 1000, read_buf_len = 4096)

while(1):

    read_data = uart_A.read()#读取串口字节类型数据
    if read_data:
        read_str = read_data.decode('utf-8')#将字节类型数据解码成字符串数据
        uart_A.write(read_str)
    if read_data:
        print("receive")
