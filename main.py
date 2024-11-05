import time
import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system

# Define the pin for 0
led_pin = board.get_pin('d:6:0') 
board.digital[6].mode = 1


# Run for 10 seconds, changing the brightness
while True:
    led_pin.write(True)  # Convert to 0.0 - 1.0 range
    time.sleep(0.1)  # Wait for 100 milliseconds
    led_pin.write(False)  # Convert to 0.0 - 1.0 range
    # time.sleep(0.1)  # Wait for 100 milliseconds

