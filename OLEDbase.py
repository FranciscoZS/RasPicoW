from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
import framebuf
from time import sleep
from utime import sleep_ms

spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18)) #mosi[TX] sck[sck]
oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))
#oled = SSD1306_SPI(WIDTH, HEIGHT, spi, dc[CSn],rst, cs[rx]) use GPIO PIN NUMBERS
while True:    
                oled.fill(0)
                oled.show()
                #sleep(1)
                oled.text("HELLO WORLD",0,10,1)
                oled.show()
                sleep_ms(100)
