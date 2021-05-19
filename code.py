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
        value = input()
        print(value)
        pixels[1] = (int(value) * percentOfRGB, 255 - int(value) * percentOfRGB, 0)
    else:
        pixels[0] = (0, 0, 0)
