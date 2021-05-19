import board
import digitalio
import time
import neopixel
import supervisor
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)
pixels.fill((0,0,0))
pixels.brightness = 0.1
percentOfRGB = 255 / 100

print('USB Connected: ', supervisor.runtime.usb_connected)
while True:
    if supervisor.runtime.serial_bytes_available:
        pixels[0] = (0, 255, 0)
        value = input().split()
        print(value)
        pixels[1] = (int(value[0]) * percentOfRGB, 255 - int(value[0]) * percentOfRGB, 0) #cpu
        pixels[2] = (int(value[1]) * percentOfRGB, 255 - int(value[1]) * percentOfRGB, 0) # memory
        pixels[3] = (int(value[2]) * percentOfRGB, 255 - int(value[2]) * percentOfRGB, 0) # disk
    else:
        pixels[0] = (0, 0, 0)
