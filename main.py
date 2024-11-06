import time
import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system

# Define the digital pin 6 as output
# led_pin = board.get_pin('d:6:o')

# Define the digital pin 6 as pwm
LED = board.digital[9]
LED.mode = 3

print("CODE INIT")

while True:
    # Simple blinking code
    # led_pin.write(True)  
    # time.sleep(0.1)
    # led_pin.write(False) 
    # time.sleep(0.1)

    for i in range(0, 256):  # i ranges from 0 to 100
        dt = i/255
        print("DT: ", dt)
        LED.write(dt)
        print("Iteration: ", i)
        time.sleep(0.1)  # small delay