import time

import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system

# Define the LED pin 
led_pin = board.get_pin('d:6:0')

# Define the mode: Output=1, Input=2, PWM=3
board.digital[6].mode = 1

while True:
    led_pin.write(True)  # Convert to 0.0 - 1.0 range
    time.sleep(0.5)  # Wait for 100 milliseconds
    led_pin.write(False)
