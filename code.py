import board
import digitalio
import time
import neopixel
import supervisor
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)
pixels.fill((0,0,0))
pixels.brightness = 0.01

print('USB Connected: ', supervisor.runtime.usb_connected)
while True:
    print('loop')
    if supervisor.runtime.serial_bytes_available:
        #print('data')
        value = input()
        print(value)
    pixels[3] = (255, 0, 0)
    pixels[1] = (255, 0, 0)
    #pixels.fill((255, 0, 0))
    #time.sleep(0.5)
    #pixels.fill((0, 0, 0))
    #time.sleep(0.5)
