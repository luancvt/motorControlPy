import time
import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system


# # Define the PWM pin (for example, pin 9)
# pwm_pin = board.get_pin('d:6:p')  # 'd' for digital, '9' for pin number, 'p' for PWM

# pwm_value = 0.5  # 50% duty cycle (0.0 to 1.0)
# pwm_pin.write(pwm_value)  # Write PWM value to the pin

# # Run for 10 seconds, changing the brightness
# while True:
#     for value in range(0, 256, 5):  # Gradually increase brightness
#         pwm_pin.write(value / 255.0)  # Convert to 0.0 - 1.0 range
#         time.sleep(0.1)  # Wait for 100 milliseconds

#     for value in range(255, -1, -5):  # Gradually decrease brightness
#         pwm_pin.write(value / 255.0)  # Convert to 0.0 - 1.0 range
#         time.sleep(0.1)  # Wait for 100 milliseconds

#port = 'COM3'# Windows
port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401'# Mac

HIGH = True# Create a high state for turn on led 
LOW = False # Create a low state for turn off led 
board = pyfirmata.Arduino(port) # Initialize the communication with the Arduino card
LED_pin = board.get_pin('d:16:o') # Initialize the pin (d => digital, 8 => Number of the pin, o => output)

for i in range(10): # Loop to blink the micro-led dix times
    LED_pin.write(HIGH) # Turn on the led
    time.sleep(0.5) # Delay of 0.5 seconds
    LED_pin.write(LOW) # Turn off the led
    time.sleep(0.5) # Delay of 0.5 seconds

board.exit() # Closing the communication with the Arduino card