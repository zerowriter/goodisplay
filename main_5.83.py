import machine
import utime
import framebuf
#EPD GPIO
isEPD_W21_BUSY=machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN) #BUSY
EPD_W21_RST= machine.Pin(1, machine.Pin.OUT)#RESE
EPD_W21_DC= machine.Pin(2, machine.Pin.OUT)#DC
EPD_W21_CS= machine.Pin(3, machine.Pin.OUT)#CS
#SPI0
spi_sck=machine.Pin(6) #SCLK
spi_tx=machine.Pin(7)#SDIN
spi_rx=machine.Pin(4)
spi=machine.SPI(0,baudrate=10000000,sck=spi_sck, mosi=spi_tx, miso=spi_rx) #10Mhz
#LED
led_onboard = machine.Pin(25, machine.Pin.OUT)
gImage_00 =[
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XE0,0X07,0XFF,0XFF,0XFF,0XFF,0X80,0X01,0XFF,0XFF,0XFF,0XFE,0X03,0XC0,
0X7F,0XFF,0XFF,0XFC,0X07,0XF0,0X3F,0XFF,0XFF,0XF8,0X0F,0XF8,0X1F,0XFF,0XFF,0XF0,
0X1F,0XFC,0X0F,0XFF,0XFF,0XE0,0X3F,0XFC,0X07,0XFF,0XFF,0XC0,0X7F,0XFE,0X03,0XFF,
0XFF,0XC0,0X7F,0XFE,0X03,0XFF,0XFF,0X80,0XFF,0XFF,0X01,0XFF,0XFF,0X00,0XFF,0XFF,
0X01,0XFF,0XFF,0X01,0XFF,0XFF,0X80,0XFF,0XFE,0X01,0XFF,0XFF,0X80,0XFF,0XFE,0X01,
0XFF,0XFF,0X80,0X7F,0XFE,0X03,0XFF,0XFF,0X80,0X7F,0XFC,0X03,0XFF,0XFF,0XC0,0X3F,
0XFC,0X03,0XFF,0XFF,0XC0,0X3F,0XFC,0X03,0XFF,0XFF,0XC0,0X3F,0XF8,0X03,0XFF,0XFF,
0XC0,0X3F,0XF8,0X07,0XFF,0XFF,0XC0,0X1F,0XF8,0X07,0XFF,0XFF,0XE0,0X1F,0XF8,0X07,
0XFF,0XFF,0XE0,0X1F,0XF8,0X07,0XFF,0XFF,0XE0,0X1F,0XF0,0X07,0XFF,0XFF,0XE0,0X1F,
0XF0,0X07,0XFF,0XFF,0XE0,0X1F,0XF0,0X07,0XFF,0XFF,0XE0,0X0F,0XF0,0X07,0XFF,0XFF,
0XE0,0X0F,0XF0,0X07,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,
0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,
0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,
0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,0XFF,0XFF,0XE0,0X0F,0XF0,0X0F,
0XFF,0XFF,0XE0,0X0F,0XF0,0X07,0XFF,0XFF,0XE0,0X0F,0XF0,0X07,0XFF,0XFF,0XE0,0X0F,
0XF0,0X07,0XFF,0XFF,0XE0,0X1F,0XF0,0X07,0XFF,0XFF,0XE0,0X1F,0XF0,0X07,0XFF,0XFF,
0XE0,0X1F,0XF8,0X07,0XFF,0XFF,0XE0,0X1F,0XF8,0X07,0XFF,0XFF,0XE0,0X1F,0XF8,0X07,
0XFF,0XFF,0XE0,0X1F,0XF8,0X07,0XFF,0XFF,0XC0,0X1F,0XF8,0X03,0XFF,0XFF,0XC0,0X3F,
0XFC,0X03,0XFF,0XFF,0XC0,0X3F,0XFC,0X03,0XFF,0XFF,0XC0,0X3F,0XFC,0X03,0XFF,0XFF,
0XC0,0X7F,0XFE,0X03,0XFF,0XFF,0X80,0X7F,0XFE,0X01,0XFF,0XFF,0X80,0X7F,0XFE,0X01,
0XFF,0XFF,0X80,0XFF,0XFF,0X01,0XFF,0XFF,0X80,0XFF,0XFF,0X00,0XFF,0XFF,0X01,0XFF,
0XFF,0X80,0XFF,0XFF,0X01,0XFF,0XFF,0X80,0X7F,0XFE,0X03,0XFF,0XFF,0XC0,0X7F,0XFE,
0X03,0XFF,0XFF,0XE0,0X3F,0XFC,0X07,0XFF,0XFF,0XF0,0X1F,0XFC,0X0F,0XFF,0XFF,0XF8,
0X1F,0XF8,0X1F,0XFF,0XFF,0XFC,0X07,0XF0,0X3F,0XFF,0XFF,0XFE,0X03,0XC0,0X7F,0XFF,
0XFF,0XFF,0X80,0X01,0XFF,0XFF,0XFF,0XFF,0XE0,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_11 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0X8F,0XFF,0XFF,0XFF,0XFF,0XFF,0X0F,0XFF,0XFF,0XFF,0XFF,0XFE,0X0F,
0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XC0,0X0F,0XFF,0XFF,0XFF,0XC0,0X00,0X0F,0XFF,0XFF,0XFF,0XC0,0X00,0X0F,0XFF,0XFF,
0XFF,0XFF,0XE0,0X0F,0XFF,0XFF,0XFF,0XFF,0XF0,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF0,0X0F,
0XFF,0XFF,0XFF,0XFF,0XF0,0X07,0XFF,0XFF,0XFF,0XFF,0XF0,0X07,0XFF,0XFF,0XFF,0XFF,
0XE0,0X03,0XFF,0XFF,0XFF,0XFF,0X80,0X00,0XFF,0XFF,0XFF,0XC0,0X00,0X00,0X01,0XFF,
0XFF,0XC0,0X00,0X00,0X01,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_22 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XE0,0X03,0XFF,0XFF,0XFF,0XFF,0X00,0X00,0X7F,0XFF,0XFF,0XF8,0X0F,0XC0,
0X1F,0XFF,0XFF,0XF0,0X3F,0XF8,0X07,0XFF,0XFF,0XC0,0XFF,0XFC,0X03,0XFF,0XFF,0X81,
0XFF,0XFE,0X01,0XFF,0XFF,0X03,0XFF,0XFF,0X01,0XFF,0XFF,0X03,0XFF,0XFF,0X00,0XFF,
0XFE,0X07,0XFF,0XFF,0X80,0XFF,0XFE,0X07,0XFF,0XFF,0X80,0X7F,0XFC,0X07,0XFF,0XFF,
0X80,0X7F,0XFC,0X07,0XFF,0XFF,0XC0,0X3F,0XFC,0X07,0XFF,0XFF,0XC0,0X3F,0XF8,0X07,
0XFF,0XFF,0XC0,0X3F,0XF8,0X03,0XFF,0XFF,0XC0,0X3F,0XF8,0X03,0XFF,0XFF,0XC0,0X3F,
0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X01,0XFF,0XFF,
0XC0,0X3F,0XFC,0X01,0XFF,0XFF,0XC0,0X3F,0XFC,0X01,0XFF,0XFF,0XC0,0X7F,0XFF,0X03,
0XFF,0XFF,0X80,0X7F,0XFF,0XFF,0XFF,0XFF,0X80,0X7F,0XFF,0XFF,0XFF,0XFF,0X80,0XFF,
0XFF,0XFF,0XFF,0XFF,0X00,0XFF,0XFF,0XFF,0XFF,0XFF,0X00,0XFF,0XFF,0XFF,0XFF,0XFE,
0X01,0XFF,0XFF,0XFF,0XFF,0XFE,0X03,0XFF,0XFF,0XFF,0XFF,0XFC,0X03,0XFF,0XFF,0XFF,
0XFF,0XFC,0X07,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,
0XFF,0XFF,0XFF,0XE0,0X3F,0XFF,0XFF,0XFF,0XFF,0XE0,0X7F,0XFF,0XFF,0XFF,0XFF,0XC0,
0XFF,0XFF,0XFF,0XFF,0XFF,0X81,0XFF,0XFF,0XFF,0XFF,0XFF,0X03,0XFF,0XFF,0XFF,0XFF,
0XFE,0X07,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X1F,0XFF,0XFF,
0XFF,0XFF,0XF0,0X3F,0XFF,0XFF,0XFF,0XFF,0XE0,0X7F,0XFF,0XFF,0XFF,0XFF,0XC0,0XFF,
0XFF,0XFF,0XFF,0XFF,0X81,0XFF,0XFF,0XFF,0XFF,0XFF,0X03,0XFF,0XFF,0XFF,0XFF,0XFE,
0X07,0XFF,0XFF,0XFF,0XFF,0XFE,0X0F,0XFF,0XFF,0XFF,0XFF,0XFC,0X1F,0XFF,0XFF,0XFF,
0XFF,0XF8,0X3F,0XFF,0XFE,0X1F,0XFF,0XF0,0X7F,0XFF,0XFE,0X1F,0XFF,0XE0,0XFF,0XFF,
0XFE,0X3F,0XFF,0XC0,0XFF,0XFF,0XFC,0X3F,0XFF,0X81,0XFF,0XFF,0XFC,0X3F,0XFF,0X83,
0XFF,0XFF,0XFC,0X3F,0XFF,0X07,0XFF,0XFF,0XF8,0X3F,0XFE,0X0F,0XFF,0XFF,0XF8,0X3F,
0XFC,0X1F,0XFF,0XFF,0XF0,0X3F,0XFC,0X1F,0XFF,0XFF,0XE0,0X7F,0XF8,0X3F,0XFF,0XFF,
0X80,0X7F,0XF0,0X00,0X00,0X00,0X00,0X7F,0XF0,0X00,0X00,0X00,0X00,0X7F,0XF0,0X00,
0X00,0X00,0X00,0X7F,0XF0,0X00,0X00,0X00,0X00,0X7F,0XF0,0X00,0X00,0X00,0X00,0X7F,
0XF0,0X00,0X00,0X00,0X00,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_33 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XC0,0X0F,0XFF,0XFF,0XFF,0XFC,0X00,0X01,0XFF,0XFF,0XFF,0XF0,0X1F,0X00,
0X7F,0XFF,0XFF,0XE0,0XFF,0XE0,0X3F,0XFF,0XFF,0XC1,0XFF,0XF0,0X1F,0XFF,0XFF,0X83,
0XFF,0XF8,0X0F,0XFF,0XFF,0X03,0XFF,0XFC,0X07,0XFF,0XFE,0X03,0XFF,0XFC,0X03,0XFF,
0XFE,0X03,0XFF,0XFE,0X03,0XFF,0XFC,0X03,0XFF,0XFE,0X01,0XFF,0XFC,0X03,0XFF,0XFF,
0X01,0XFF,0XFC,0X03,0XFF,0XFF,0X00,0XFF,0XFC,0X01,0XFF,0XFF,0X00,0XFF,0XFC,0X01,
0XFF,0XFF,0X00,0XFF,0XFC,0X01,0XFF,0XFF,0X00,0XFF,0XFC,0X01,0XFF,0XFF,0X00,0XFF,
0XFE,0X03,0XFF,0XFF,0X00,0XFF,0XFF,0X03,0XFF,0XFF,0X00,0XFF,0XFF,0XFF,0XFF,0XFF,
0X00,0XFF,0XFF,0XFF,0XFF,0XFF,0X00,0XFF,0XFF,0XFF,0XFF,0XFF,0X01,0XFF,0XFF,0XFF,
0XFF,0XFE,0X01,0XFF,0XFF,0XFF,0XFF,0XFE,0X01,0XFF,0XFF,0XFF,0XFF,0XFE,0X03,0XFF,
0XFF,0XFF,0XFF,0XFC,0X07,0XFF,0XFF,0XFF,0XFF,0XF8,0X07,0XFF,0XFF,0XFF,0XFF,0XF0,
0X0F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XC0,0X7F,0XFF,0XFF,0XFF,
0XFE,0X01,0XFF,0XFF,0XFF,0XFF,0XC0,0X07,0XFF,0XFF,0XFF,0XFF,0XC0,0X01,0XFF,0XFF,
0XFF,0XFF,0XFF,0X00,0X7F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF8,
0X0F,0XFF,0XFF,0XFF,0XFF,0XFC,0X07,0XFF,0XFF,0XFF,0XFF,0XFE,0X03,0XFF,0XFF,0XFF,
0XFF,0XFF,0X01,0XFF,0XFF,0XFF,0XFF,0XFF,0X00,0XFF,0XFF,0XFF,0XFF,0XFF,0X80,0XFF,
0XFF,0XFF,0XFF,0XFF,0X80,0X7F,0XFF,0XFF,0XFF,0XFF,0XC0,0X7F,0XFF,0XFF,0XFF,0XFF,
0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,
0XFF,0XFF,0XC0,0X1F,0XFF,0XFF,0XFF,0XFF,0XC0,0X1F,0XFF,0XFF,0XFF,0XFF,0XC0,0X1F,
0XFF,0X07,0XFF,0XFF,0XC0,0X1F,0XFE,0X03,0XFF,0XFF,0XC0,0X1F,0XFC,0X03,0XFF,0XFF,
0XC0,0X1F,0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X01,
0XFF,0XFF,0XC0,0X3F,0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X03,0XFF,0XFF,0X80,0X7F,
0XF8,0X03,0XFF,0XFF,0X80,0X7F,0XFC,0X03,0XFF,0XFF,0X80,0XFF,0XFC,0X03,0XFF,0XFF,
0X01,0XFF,0XFE,0X03,0XFF,0XFE,0X03,0XFF,0XFF,0X03,0XFF,0XFE,0X03,0XFF,0XFF,0X81,
0XFF,0XFC,0X07,0XFF,0XFF,0XC0,0XFF,0XF0,0X1F,0XFF,0XFF,0XF0,0X1F,0X80,0X3F,0XFF,
0XFF,0XFC,0X00,0X00,0XFF,0XFF,0XFF,0XFF,0X80,0X0F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_44 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XF8,0X1F,0XFF,0XFF,0XFF,0XFF,0XF8,
0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,
0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XC0,0X1F,0XFF,0XFF,0XFF,0XFF,0XC0,0X1F,0XFF,
0XFF,0XFF,0XFF,0X80,0X1F,0XFF,0XFF,0XFF,0XFF,0X00,0X1F,0XFF,0XFF,0XFF,0XFF,0X00,
0X1F,0XFF,0XFF,0XFF,0XFE,0X00,0X1F,0XFF,0XFF,0XFF,0XFE,0X10,0X1F,0XFF,0XFF,0XFF,
0XFC,0X10,0X1F,0XFF,0XFF,0XFF,0XF8,0X30,0X1F,0XFF,0XFF,0XFF,0XF8,0X70,0X1F,0XFF,
0XFF,0XFF,0XF0,0X70,0X1F,0XFF,0XFF,0XFF,0XE0,0XF0,0X1F,0XFF,0XFF,0XFF,0XE1,0XF0,
0X1F,0XFF,0XFF,0XFF,0XC1,0XF0,0X1F,0XFF,0XFF,0XFF,0X83,0XF0,0X1F,0XFF,0XFF,0XFF,
0X83,0XF0,0X1F,0XFF,0XFF,0XFF,0X07,0XF0,0X1F,0XFF,0XFF,0XFF,0X0F,0XF0,0X1F,0XFF,
0XFF,0XFE,0X0F,0XF0,0X1F,0XFF,0XFF,0XFC,0X1F,0XF0,0X1F,0XFF,0XFF,0XFC,0X3F,0XF0,
0X1F,0XFF,0XFF,0XF8,0X3F,0XF0,0X1F,0XFF,0XFF,0XF0,0X7F,0XF0,0X1F,0XFF,0XFF,0XF0,
0X7F,0XF0,0X1F,0XFF,0XFF,0XE0,0XFF,0XF0,0X1F,0XFF,0XFF,0XE1,0XFF,0XF0,0X1F,0XFF,
0XFF,0XC1,0XFF,0XF0,0X1F,0XFF,0XFF,0X83,0XFF,0XF0,0X1F,0XFF,0XFF,0X87,0XFF,0XF0,
0X1F,0XFF,0XFF,0X07,0XFF,0XF0,0X1F,0XFF,0XFE,0X0F,0XFF,0XF0,0X1F,0XFF,0XFE,0X1F,
0XFF,0XF0,0X1F,0XFF,0XFC,0X1F,0XFF,0XF0,0X1F,0XFF,0XFC,0X3F,0XFF,0XF0,0X1F,0XFF,
0XF8,0X3F,0XFF,0XF0,0X1F,0XFF,0XF0,0X7F,0XFF,0XF0,0X1F,0XFF,0XF0,0XFF,0XFF,0XF0,
0X1F,0XFF,0XE0,0XFF,0XFF,0XF0,0X1F,0XFF,0XE0,0X00,0X00,0X00,0X00,0X07,0XE0,0X00,
0X00,0X00,0X00,0X07,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,
0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,
0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,
0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,
0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,
0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X0F,0XFF,0XFF,0XFF,
0XFF,0XE0,0X0F,0XFF,0XFF,0XFF,0XFF,0XC0,0X07,0XFF,0XFF,0XFF,0XC0,0X00,0X00,0X0F,
0XFF,0XFF,0XC0,0X00,0X00,0X0F,0XFF,0XFF,0XC0,0X00,0X00,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_55 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0X80,0X00,0X00,0X00,0X3F,0XFF,0X80,0X00,0X00,
0X00,0X7F,0XFF,0X80,0X00,0X00,0X00,0X7F,0XFF,0X80,0X00,0X00,0X00,0X7F,0XFF,0X80,
0X00,0X00,0X00,0X7F,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,
0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,
0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,
0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,
0XFF,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0X07,0XFF,0XFF,
0XFF,0XFF,0XFF,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0X07,
0XFF,0XFF,0XFF,0XFF,0XFF,0X0F,0XFF,0XFF,0XFF,0XFF,0XFF,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0X0F,0XF0,0X01,0XFF,0XFF,0XFF,0X0F,0X80,0X00,0X7F,0XFF,0XFF,0X0E,0X00,0X00,
0X1F,0XFF,0XFF,0X0C,0X00,0X00,0X0F,0XFF,0XFF,0X08,0X07,0XE0,0X07,0XFF,0XFF,0X00,
0X3F,0XF8,0X03,0XFF,0XFF,0X00,0XFF,0XFC,0X01,0XFF,0XFF,0X01,0XFF,0XFE,0X00,0XFF,
0XFF,0X03,0XFF,0XFF,0X00,0XFF,0XFF,0X03,0XFF,0XFF,0X00,0X7F,0XFF,0X07,0XFF,0XFF,
0X80,0X7F,0XFF,0XCF,0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,
0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,
0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,
0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,
0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0X07,0XFF,0XFF,0XE0,0X1F,
0XFC,0X03,0XFF,0XFF,0XE0,0X3F,0XFC,0X01,0XFF,0XFF,0XE0,0X3F,0XF8,0X01,0XFF,0XFF,
0XE0,0X3F,0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X01,0XFF,0XFF,0XC0,0X3F,0XF8,0X01,
0XFF,0XFF,0XC0,0X7F,0XF8,0X03,0XFF,0XFF,0XC0,0X7F,0XF8,0X07,0XFF,0XFF,0X80,0X7F,
0XFC,0X07,0XFF,0XFF,0X80,0XFF,0XFC,0X07,0XFF,0XFF,0X80,0XFF,0XFE,0X07,0XFF,0XFF,
0X01,0XFF,0XFE,0X07,0XFF,0XFE,0X03,0XFF,0XFF,0X03,0XFF,0XFE,0X03,0XFF,0XFF,0X81,
0XFF,0XFC,0X07,0XFF,0XFF,0XE0,0XFF,0XF0,0X0F,0XFF,0XFF,0XF0,0X0F,0XC0,0X3F,0XFF,
0XFF,0XFC,0X00,0X00,0XFF,0XFF,0XFF,0XFF,0X80,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_66 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFE,0X00,0X7F,0XFF,0XFF,0XFF,0XE0,0X00,0X1F,0XFF,0XFF,0XFF,0X80,0XFC,
0X07,0XFF,0XFF,0XFF,0X03,0XFE,0X03,0XFF,0XFF,0XFC,0X0F,0XFE,0X01,0XFF,0XFF,0XF8,
0X1F,0XFE,0X01,0XFF,0XFF,0XF0,0X3F,0XFE,0X00,0XFF,0XFF,0XE0,0X7F,0XFE,0X00,0XFF,
0XFF,0XE0,0XFF,0XFE,0X00,0XFF,0XFF,0XC0,0XFF,0XFE,0X00,0XFF,0XFF,0X81,0XFF,0XFE,
0X00,0XFF,0XFF,0X81,0XFF,0XFF,0X00,0XFF,0XFF,0X01,0XFF,0XFF,0X81,0XFF,0XFF,0X03,
0XFF,0XFF,0XFF,0XFF,0XFE,0X03,0XFF,0XFF,0XFF,0XFF,0XFE,0X03,0XFF,0XFF,0XFF,0XFF,
0XFC,0X03,0XFF,0XFF,0XFF,0XFF,0XFC,0X07,0XFF,0XFF,0XFF,0XFF,0XFC,0X07,0XFF,0XFF,
0XFF,0XFF,0XFC,0X07,0XFF,0XFF,0XFF,0XFF,0XF8,0X07,0XFF,0XFF,0XFF,0XFF,0XF8,0X07,
0XFF,0XFF,0XFF,0XFF,0XF8,0X07,0XFF,0XFF,0XFF,0XFF,0XF8,0X07,0XFF,0XFF,0XFF,0XFF,
0XF8,0X07,0XFC,0X00,0XFF,0XFF,0XF0,0X07,0XE0,0X00,0X1F,0XFF,0XF0,0X07,0X80,0X00,
0X0F,0XFF,0XF0,0X07,0X00,0X00,0X03,0XFF,0XF0,0X0C,0X01,0XF0,0X01,0XFF,0XF0,0X0C,
0X0F,0XFC,0X00,0XFF,0XF0,0X08,0X1F,0XFE,0X00,0XFF,0XF0,0X00,0X3F,0XFF,0X00,0X7F,
0XF0,0X00,0X7F,0XFF,0X80,0X7F,0XF0,0X00,0XFF,0XFF,0XC0,0X3F,0XF0,0X01,0XFF,0XFF,
0XC0,0X3F,0XF0,0X03,0XFF,0XFF,0XE0,0X1F,0XF0,0X03,0XFF,0XFF,0XE0,0X1F,0XF0,0X07,
0XFF,0XFF,0XE0,0X1F,0XF0,0X07,0XFF,0XFF,0XE0,0X1F,0XF0,0X0F,0XFF,0XFF,0XF0,0X0F,
0XF0,0X0F,0XFF,0XFF,0XF0,0X0F,0XF0,0X0F,0XFF,0XFF,0XF0,0X0F,0XF0,0X0F,0XFF,0XFF,
0XF0,0X0F,0XF0,0X07,0XFF,0XFF,0XF0,0X0F,0XF0,0X07,0XFF,0XFF,0XF0,0X0F,0XF0,0X07,
0XFF,0XFF,0XF0,0X0F,0XF8,0X07,0XFF,0XFF,0XF0,0X0F,0XF8,0X07,0XFF,0XFF,0XF0,0X0F,
0XF8,0X07,0XFF,0XFF,0XF0,0X0F,0XF8,0X07,0XFF,0XFF,0XF0,0X1F,0XFC,0X03,0XFF,0XFF,
0XF0,0X1F,0XFC,0X03,0XFF,0XFF,0XF0,0X1F,0XFC,0X03,0XFF,0XFF,0XE0,0X1F,0XFE,0X03,
0XFF,0XFF,0XE0,0X1F,0XFE,0X01,0XFF,0XFF,0XE0,0X3F,0XFE,0X01,0XFF,0XFF,0XE0,0X3F,
0XFF,0X00,0XFF,0XFF,0XE0,0X7F,0XFF,0X80,0XFF,0XFF,0XC0,0X7F,0XFF,0X80,0X7F,0XFF,
0XC0,0XFF,0XFF,0XC0,0X3F,0XFF,0X81,0XFF,0XFF,0XE0,0X3F,0XFF,0X03,0XFF,0XFF,0XF0,
0X0F,0XFE,0X07,0XFF,0XFF,0XF8,0X07,0XFC,0X0F,0XFF,0XFF,0XFC,0X01,0XF0,0X1F,0XFF,
0XFF,0XFF,0X00,0X00,0X7F,0XFF,0XFF,0XFF,0XE0,0X03,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_77 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0X00,0X00,0X00,0X00,0X1F,0XFF,0X00,0X00,0X00,
0X00,0X1F,0XFE,0X00,0X00,0X00,0X00,0X1F,0XFE,0X00,0X00,0X00,0X00,0X1F,0XFE,0X00,
0X00,0X00,0X00,0X3F,0XFE,0X00,0XFF,0XFF,0XF0,0X7F,0XFE,0X03,0XFF,0XFF,0XF0,0X7F,
0XFE,0X07,0XFF,0XFF,0XE0,0XFF,0XFC,0X0F,0XFF,0XFF,0XC0,0XFF,0XFC,0X1F,0XFF,0XFF,
0XC1,0XFF,0XFC,0X1F,0XFF,0XFF,0X81,0XFF,0XFC,0X3F,0XFF,0XFF,0X83,0XFF,0XFC,0X3F,
0XFF,0XFF,0X07,0XFF,0XFC,0X3F,0XFF,0XFF,0X07,0XFF,0XF8,0X7F,0XFF,0XFE,0X0F,0XFF,
0XF8,0X7F,0XFF,0XFE,0X0F,0XFF,0XFF,0XFF,0XFF,0XFC,0X1F,0XFF,0XFF,0XFF,0XFF,0XFC,
0X1F,0XFF,0XFF,0XFF,0XFF,0XF8,0X3F,0XFF,0XFF,0XFF,0XFF,0XF8,0X3F,0XFF,0XFF,0XFF,
0XFF,0XF0,0X3F,0XFF,0XFF,0XFF,0XFF,0XF0,0X7F,0XFF,0XFF,0XFF,0XFF,0XE0,0X7F,0XFF,
0XFF,0XFF,0XFF,0XE0,0XFF,0XFF,0XFF,0XFF,0XFF,0XC0,0XFF,0XFF,0XFF,0XFF,0XFF,0XC1,
0XFF,0XFF,0XFF,0XFF,0XFF,0X81,0XFF,0XFF,0XFF,0XFF,0XFF,0X81,0XFF,0XFF,0XFF,0XFF,
0XFF,0X03,0XFF,0XFF,0XFF,0XFF,0XFF,0X03,0XFF,0XFF,0XFF,0XFF,0XFE,0X07,0XFF,0XFF,
0XFF,0XFF,0XFE,0X07,0XFF,0XFF,0XFF,0XFF,0XFE,0X07,0XFF,0XFF,0XFF,0XFF,0XFC,0X07,
0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,
0XF8,0X0F,0XFF,0XFF,0XFF,0XFF,0XF8,0X1F,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,
0XFF,0XFF,0XF0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,
0XFF,0XFF,0XFF,0XFF,0XE0,0X3F,0XFF,0XFF,0XFF,0XFF,0XE0,0X3F,0XFF,0XFF,0XFF,0XFF,
0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,
0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0X80,0X3F,
0XFF,0XFF,0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,
0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFF,0XFF,
0XFF,0XFF,0X00,0X3F,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,
0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFF,0XFF,0XFF,0XFF,
0X00,0X3F,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFF,0XFF,0XFF,0XFF,0X80,0X3F,0XFF,0XFF,
0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0XE0,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_88 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XC0,0X03,0XFF,0XFF,0XFF,0XFE,0X00,0X00,0X7F,0XFF,0XFF,0XF8,0X0F,0XE0,
0X1F,0XFF,0XFF,0XE0,0X7F,0XFC,0X0F,0XFF,0XFF,0XC0,0XFF,0XFE,0X07,0XFF,0XFF,0X81,
0XFF,0XFF,0X03,0XFF,0XFF,0X03,0XFF,0XFF,0X81,0XFF,0XFE,0X07,0XFF,0XFF,0XC0,0XFF,
0XFE,0X07,0XFF,0XFF,0XC0,0X7F,0XFC,0X0F,0XFF,0XFF,0XE0,0X7F,0XFC,0X0F,0XFF,0XFF,
0XE0,0X3F,0XF8,0X0F,0XFF,0XFF,0XE0,0X3F,0XF8,0X0F,0XFF,0XFF,0XE0,0X3F,0XF8,0X0F,
0XFF,0XFF,0XF0,0X3F,0XF8,0X0F,0XFF,0XFF,0XF0,0X3F,0XF8,0X0F,0XFF,0XFF,0XF0,0X3F,
0XF8,0X0F,0XFF,0XFF,0XF0,0X3F,0XF8,0X0F,0XFF,0XFF,0XF0,0X3F,0XF8,0X07,0XFF,0XFF,
0XE0,0X3F,0XF8,0X03,0XFF,0XFF,0XE0,0X3F,0XFC,0X03,0XFF,0XFF,0XE0,0X7F,0XFC,0X01,
0XFF,0XFF,0XC0,0X7F,0XFE,0X00,0XFF,0XFF,0XC0,0XFF,0XFE,0X00,0X7F,0XFF,0X80,0XFF,
0XFF,0X00,0X1F,0XFF,0X81,0XFF,0XFF,0X80,0X0F,0XFF,0X03,0XFF,0XFF,0XC0,0X03,0XFE,
0X07,0XFF,0XFF,0XE0,0X00,0XFC,0X0F,0XFF,0XFF,0XF0,0X00,0X30,0X1F,0XFF,0XFF,0XF8,
0X00,0X00,0X7F,0XFF,0XFF,0XFE,0X00,0X00,0XFF,0XFF,0XFF,0XFE,0X00,0X00,0XFF,0XFF,
0XFF,0XF8,0X00,0X00,0X7F,0XFF,0XFF,0XF0,0X30,0X00,0X1F,0XFF,0XFF,0XE0,0X7C,0X00,
0X0F,0XFF,0XFF,0X80,0XFF,0X00,0X07,0XFF,0XFF,0X01,0XFF,0XC0,0X03,0XFF,0XFF,0X03,
0XFF,0XE0,0X01,0XFF,0XFE,0X03,0XFF,0XF8,0X00,0XFF,0XFC,0X07,0XFF,0XFC,0X00,0XFF,
0XFC,0X0F,0XFF,0XFE,0X00,0X7F,0XF8,0X0F,0XFF,0XFF,0X00,0X7F,0XF8,0X1F,0XFF,0XFF,
0X80,0X3F,0XF0,0X1F,0XFF,0XFF,0XC0,0X3F,0XF0,0X1F,0XFF,0XFF,0XC0,0X1F,0XF0,0X1F,
0XFF,0XFF,0XE0,0X1F,0XF0,0X3F,0XFF,0XFF,0XE0,0X1F,0XE0,0X3F,0XFF,0XFF,0XF0,0X1F,
0XE0,0X3F,0XFF,0XFF,0XF0,0X1F,0XE0,0X3F,0XFF,0XFF,0XF0,0X1F,0XE0,0X3F,0XFF,0XFF,
0XF0,0X1F,0XE0,0X3F,0XFF,0XFF,0XF0,0X1F,0XF0,0X3F,0XFF,0XFF,0XF0,0X1F,0XF0,0X3F,
0XFF,0XFF,0XF0,0X1F,0XF0,0X1F,0XFF,0XFF,0XF0,0X3F,0XF8,0X1F,0XFF,0XFF,0XE0,0X3F,
0XF8,0X1F,0XFF,0XFF,0XE0,0X7F,0XFC,0X0F,0XFF,0XFF,0XE0,0X7F,0XFC,0X07,0XFF,0XFF,
0XC0,0XFF,0XFE,0X07,0XFF,0XFF,0X81,0XFF,0XFF,0X03,0XFF,0XFF,0X83,0XFF,0XFF,0X80,
0XFF,0XFE,0X07,0XFF,0XFF,0XE0,0X7F,0XFC,0X0F,0XFF,0XFF,0XF0,0X0F,0XE0,0X1F,0XFF,
0XFF,0XFC,0X00,0X00,0X7F,0XFF,0XFF,0XFF,0XC0,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]
gImage_99 = [
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X80,0X0F,0XFF,0XFF,0XFF,0XFC,0X00,0X01,0XFF,0XFF,0XFF,0XF0,0X0F,0XC0,
0X7F,0XFF,0XFF,0XE0,0X3F,0XF0,0X1F,0XFF,0XFF,0XC0,0XFF,0XFC,0X0F,0XFF,0XFF,0X81,
0XFF,0XFE,0X07,0XFF,0XFF,0X01,0XFF,0XFE,0X07,0XFF,0XFE,0X03,0XFF,0XFF,0X03,0XFF,
0XFE,0X07,0XFF,0XFF,0X01,0XFF,0XFC,0X07,0XFF,0XFF,0X81,0XFF,0XF8,0X07,0XFF,0XFF,
0X80,0XFF,0XF8,0X0F,0XFF,0XFF,0XC0,0XFF,0XF8,0X0F,0XFF,0XFF,0XC0,0X7F,0XF0,0X0F,
0XFF,0XFF,0XC0,0X7F,0XF0,0X0F,0XFF,0XFF,0XC0,0X3F,0XF0,0X0F,0XFF,0XFF,0XC0,0X3F,
0XF0,0X1F,0XFF,0XFF,0XE0,0X3F,0XF0,0X1F,0XFF,0XFF,0XE0,0X3F,0XE0,0X1F,0XFF,0XFF,
0XE0,0X1F,0XE0,0X1F,0XFF,0XFF,0XE0,0X1F,0XE0,0X1F,0XFF,0XFF,0XE0,0X1F,0XE0,0X1F,
0XFF,0XFF,0XE0,0X1F,0XE0,0X1F,0XFF,0XFF,0XE0,0X1F,0XE0,0X1F,0XFF,0XFF,0XE0,0X1F,
0XF0,0X0F,0XFF,0XFF,0XE0,0X1F,0XF0,0X0F,0XFF,0XFF,0XC0,0X1F,0XF0,0X0F,0XFF,0XFF,
0XC0,0X1F,0XF0,0X0F,0XFF,0XFF,0X80,0X1F,0XF0,0X0F,0XFF,0XFF,0X80,0X1F,0XF0,0X07,
0XFF,0XFF,0X00,0X1F,0XF8,0X07,0XFF,0XFF,0X00,0X1F,0XF8,0X03,0XFF,0XFE,0X00,0X1F,
0XF8,0X03,0XFF,0XFC,0X00,0X1F,0XFC,0X01,0XFF,0XF8,0X00,0X1F,0XFC,0X00,0XFF,0XF0,
0X20,0X1F,0XFE,0X00,0X7F,0XE0,0X60,0X1F,0XFF,0X00,0X1F,0X00,0XE0,0X1F,0XFF,0X80,
0X00,0X01,0XC0,0X1F,0XFF,0XE0,0X00,0X03,0XC0,0X1F,0XFF,0XF0,0X00,0X0F,0XC0,0X1F,
0XFF,0XFE,0X00,0X3F,0XC0,0X1F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,
0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X3F,0XFF,0XFF,
0XFF,0XFF,0X80,0X3F,0XFF,0XFF,0XFF,0XFF,0X80,0X7F,0XFF,0XFF,0XFF,0XFF,0X80,0X7F,
0XFF,0XFF,0XFF,0XFF,0X80,0X7F,0XFF,0XFF,0XFF,0XFF,0X80,0XFF,0XFF,0XFF,0XFF,0XFF,
0X00,0XFF,0XFF,0XFF,0XFF,0XFF,0X01,0XFF,0XFF,0XFF,0XFF,0XFF,0X01,0XFF,0XFF,0X83,
0XFF,0XFE,0X03,0XFF,0XFF,0X01,0XFF,0XFE,0X03,0XFF,0XFE,0X00,0XFF,0XFC,0X07,0XFF,
0XFE,0X00,0XFF,0XFC,0X07,0XFF,0XFE,0X00,0XFF,0XF8,0X0F,0XFF,0XFE,0X00,0XFF,0XF8,
0X1F,0XFF,0XFE,0X00,0XFF,0XF0,0X1F,0XFF,0XFE,0X00,0XFF,0XE0,0X3F,0XFF,0XFF,0X00,
0XFF,0XC0,0X7F,0XFF,0XFF,0X80,0X7F,0X81,0XFF,0XFF,0XFF,0XC0,0X3C,0X03,0XFF,0XFF,
0XFF,0XF0,0X00,0X0F,0XFF,0XFF,0XFF,0XFC,0X00,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]




#SPI#####################
def SPI_Write(data):
    spi.write(chr(data))

def EPD_W21_WriteCMD(command):
    EPD_W21_CS.value(0) #CS               
    EPD_W21_DC.value(0) #DC
    SPI_Write(command)# command write
    EPD_W21_CS.value(1) #CS  

def EPD_W21_WriteDATA(data):
    EPD_W21_CS.value(0) #CS                       
    EPD_W21_DC.value(1) #DC
    SPI_Write(data)  # data write
    EPD_W21_CS.value(1) #CS  

#EPD IC RESET
def EPD_W21_Init():
    EPD_W21_RST.value(0) # Module reset
    utime.sleep(0.01)   #At least 10ms delay 
    EPD_W21_RST.value(1)
    utime.sleep(0.01)   #At least 10ms delay 

#BUSY
def lcd_chkstatus():
    while isEPD_W21_BUSY.value()==0:
        utime.sleep(0.01) 
#UC8179 init
def EPD_init():
    EPD_W21_Init()  #Electronic paper IC reset
   
    EPD_W21_WriteCMD(0X00)#PANNEL SETTING
    EPD_W21_WriteDATA(0x1F)   #KW-3f   KWR-2F BWROTP 0f BWOTP 1f

    EPD_W21_WriteCMD(0x04) #POWER ON 
    utime.sleep(0.3)
    lcd_chkstatus()        #waiting for the electronic paper IC to release the idle signal
    
    EPD_W21_WriteCMD(0X50) #VCOM AND DATA INTERVAL SETTING
    EPD_W21_WriteDATA(0x21)
    EPD_W21_WriteDATA(0x07)
    
#UC8179 init Fast
def EPD_init_Fast():
    EPD_W21_Init()  #Electronic paper IC reset
   
    EPD_W21_WriteCMD(0X00) #PANNEL SETTING
    EPD_W21_WriteDATA(0x1F)   #KW-3f   KWR-2F BWROTP 0f BWOTP 1f

    EPD_W21_WriteCMD(0x04) #POWER ON 
    utime.sleep(0.3)
    lcd_chkstatus()        #waiting for the electronic paper IC to release the idle signal
    
    EPD_W21_WriteCMD(0X50) #VCOM AND DATA INTERVAL SETTING
    EPD_W21_WriteDATA(0x29)
    EPD_W21_WriteDATA(0x07)
    
    EPD_W21_WriteCMD(0xE0)
    EPD_W21_WriteDATA(0x02)
    EPD_W21_WriteCMD(0xE5)
    EPD_W21_WriteDATA(0x5A)    
 
 #UC8179 init Fast
def EPD_display_init():
    EPD_W21_Init()  #Electronic paper IC reset
   
    EPD_W21_WriteCMD(0X00) #PANNEL SETTING
    EPD_W21_WriteDATA(0x1F)   #KW-3f   KWR-2F BWROTP 0f BWOTP 1f

    EPD_W21_WriteCMD(0x04) #POWER ON 
    utime.sleep(0.3)
    lcd_chkstatus()        #waiting for the electronic paper IC to release the idle signal
  
    EPD_W21_WriteCMD(0X50) #VCOM AND DATA INTERVAL SETTING
    EPD_W21_WriteDATA(0x29)
    EPD_W21_WriteDATA(0x07)
    
    EPD_W21_WriteCMD(0xE0)
    EPD_W21_WriteDATA(0x02)
    EPD_W21_WriteCMD(0xE5)
    EPD_W21_WriteDATA(0x6E)  


#display 
def PIC_display(picData):
    #Write Data
    EPD_W21_WriteCMD(0x10)       #Transfer old data
    for i in range(38880):
        EPD_W21_WriteDATA(0xff)

    EPD_W21_WriteCMD(0x13)    #Transfer new data
    for i in range(38880):     
        EPD_W21_WriteDATA(picData[i]) #Transfer the actual displayed data

    #Refresh
    EPD_W21_WriteCMD(0x12) #DISPLAY REFRESH
    utime.sleep(0.01)        #!!!The delay here is necessary, 200uS at least!!! 
    lcd_chkstatus()          #waiting for the electronic paper IC to release the idle signal
#Clear screen
def PIC_display_Clear():
    #Write Data
    EPD_W21_WriteCMD(0x10)       #Transfer old data
    for j in range(38880):  
        EPD_W21_WriteDATA(0xFF) 
    EPD_W21_WriteCMD(0x13)     #Transfer new data
    for j in range(38880):        
        EPD_W21_WriteDATA(0xff)  #Transfer the actual displayed data
    #Refresh
    EPD_W21_WriteCMD(0x12)#DISPLAY REFRESH 
    utime.sleep(0.01)       #!!!The delay here is necessary, 200uS at least!!!     
    lcd_chkstatus()         #waiting for the electronic paper IC to release the idle signal
#Enter deep sleep mode 
def EPD_sleep(): 
    EPD_W21_WriteCMD(0X50)  #VCOM AND DATA INTERVAL SETTING
    EPD_W21_WriteDATA(0xf7) #WBmode:VBDF 17|D7 VBDW 97 VBDB 57 WBRmode:VBDF F7 VBDW 77 VBDB 37  VBDR B7

    EPD_W21_WriteCMD(0X02) #power off
    lcd_chkstatus()          #waiting for the electronic paper IC to release the idle signal
    EPD_W21_WriteCMD(0X07) #deep sleep
    EPD_W21_WriteDATA(0xA5)
 
def EPD_partial_display(x_start,y_start,new_data,PART_COLUMN,PART_LINE,mode): #mode 0: first  1: other...
    x_end=x_start+PART_LINE-1 
    y_end=y_start+PART_COLUMN-1
    datas=PART_LINE*PART_COLUMN//8

    EPD_W21_WriteCMD(0x50)
    EPD_W21_WriteDATA(0xA9)
    EPD_W21_WriteDATA(0x07)

    EPD_W21_WriteCMD(0x91)#This command makes the display enter partial mode
    EPD_W21_WriteCMD(0x90)#resolution setting
    EPD_W21_WriteDATA (x_start//256)
    EPD_W21_WriteDATA (x_start%256) #x-start    
    
    EPD_W21_WriteDATA (x_end//256)
    EPD_W21_WriteDATA (x_end%256-1)  #x-end

    EPD_W21_WriteDATA (y_start//256)
    EPD_W21_WriteDATA (y_start%256)  #y-start    
    
    EPD_W21_WriteDATA (y_end//256)
    EPD_W21_WriteDATA (y_end%256-1) #y-end
    EPD_W21_WriteDATA (0x01);
 
    EPD_W21_WriteCMD(0x13)#writes New data to SRAM.
    for i in range(datas):        
        EPD_W21_WriteDATA(new_data[i])
     #update
    EPD_W21_WriteCMD(0x12)#DISPLAY REFRESH         
    utime.sleep(0.01)     #!!!The delay here is necessary, 200uS at least!!!     
    lcd_chkstatus() 
 
 
 
 
 
#Main function part
while True:
    #############MicroPython  GUI############### 
    width=648
    height=480 
    buffer = bytearray(height * width // 8)   
    fbuf = framebuf.FrameBuffer(buffer, width, height, framebuf.MONO_HLSB)
    fbuf.fill(0xff) #white background
    fbuf.text('www.good-display.cn', 145, 0, 0x00) #s, x, y[, c]
    fbuf.hline(145, 10, 152, 0x00)
    fbuf.text("Raspberry Pico", 165, 16, 0x00)
     #古
    fbuf.vline(213, 40, 50, 0x00)#x, y, w, c
    fbuf.hline(173, 70, 80, 0x00)#x, y, w, c
    fbuf.rect(188, 92, 50, 50, 0x00)
     
    #Picture
    EPD_init_Fast() #EPD init Fast
    PIC_display(buffer)#EPD GUI
    EPD_sleep()#EPD_sleep,Sleep instruction is necessary, please do not delete!!!
    utime.sleep(3) #delay 3s
    ###############################################     

    #Clear
    EPD_init() #EPD init
    PIC_display_Clear()#EPD Clear
    EPD_sleep()#EPD_sleep,Sleep instruction is necessary, please do not delete!!!
    utime.sleep(3) #delay 3s
    #Partial display
    EPD_display_init()
    EPD_partial_display(304,180,gImage_11,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_22,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_33,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_44,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_55,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_77,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_88,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_partial_display(304,180,gImage_99,104,48,1)#x,y,old_data,new_data,W,L,mode 
    EPD_sleep()#EPD_sleep,Sleep instruction is necessary, please do not delete!!! 
    utime.sleep(3) #delay 3s
    
    #Clear
    EPD_init() #EPD init
    PIC_display_Clear()#EPD Clear
    EPD_sleep()#EPD_sleep,Sleep instruction is necessary, please do not delete!!!
    while 1:
        led_onboard.toggle()
        utime.sleep(1) #delay 1s



 
    
    
    

   
    
    
    
