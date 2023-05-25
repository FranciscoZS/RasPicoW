from machine import Pin
import time
led_1 = Pin('LED', Pin.OUT)
while True:
    led_1.on()
    time.sleep_ms(500)
    led_1.off()
    time.sleep_ms(500)
    print("running")