import board
import digitalio
import time
import neopixel
import supervisor
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

#Turn off all LEDs
pixels.fill((0,0,0))

#Reduce brightness to prevent being blinded.
pixels.brightness = 0.1

#Calculate 1% of RGB max value
percentOfRGB = 255 / 100

#Set timeout to zero
timeout = 0

print('USB Connected: ', supervisor.runtime.usb_connected)
while True:
    
    if supervisor.runtime.serial_bytes_available:
        #If data then reset timeout 
        timeout = 0

        #Set data LED to green
        pixels[0] = (0, 255, 0)

        #Split input (Expected as 3 space seperated values (E.G. '30 10 60'))
        value = input().split()
        print(value)

        #Map each of the 3 values to an LED calculating the RGB for Red and the inverse for Green
        pixels[1] = (int(value[0]) * percentOfRGB, 255 - int(value[0]) * percentOfRGB, 0) #cpu
        pixels[2] = (int(value[1]) * percentOfRGB, 255 - int(value[1]) * percentOfRGB, 0) # memory
        pixels[3] = (int(value[2]) * percentOfRGB, 255 - int(value[2]) * percentOfRGB, 0) # disk
    else:
        # Add 1 time timeout counter if no data
        timeout += 1

        # If timeout reaches 1000 turn LEDs off
        if timeout >= 1000:
            pixels.fill((0,0,0))

        #Turn off data LED if no data
        pixels[0] = (0, 0, 0)
