import time
import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system

# Define the pin for 0
led_pin = board.get_pin('d:6:0') 
board.digital[6].mode = 1
# pwm = board.get_pin('d:6:p') 
# board.digital[6].mode = 3


while True:
    # Simple blinking code
    led_pin.write(True)  
    time.sleep(0.1)
    led_pin.write(False) 
    time.sleep(0.1)

    # for i in range(0, 101):  # i ranges from 0 to 100
    #     duty_cycle = i / 100  # convert to a range between 0 and 1
    #     board.digital[6].write(duty_cycle)  # Write PWM duty cycle to pin
    #     time.sleep(0.05)  # small delay

    # # Gradually decrease the PWM signal
    # for i in range(100, -1, -1):  # i ranges from 100 down to 0
    #     duty_cycle = i / 100
    #     board.digital[6].write(duty_cycle)
    #     time.sleep(0.05)

