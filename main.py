import time
import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system


# Define the PWM pin (for example, pin 9)
pwm_pin = board.get_pin('d:6:0')  # 'd' for digital, '9' for pin number, 'p' for PWM
board.digital[pwm_pin].mode = 1

# pwm_value = 0.5  # 50% duty cycle (0.0 to 1.0)
# pwm_pin.write(pwm_value)  # Write PWM value to the pin

# Run for 10 seconds, changing the brightness
while True:
    for value in range(0, 256, 5):  # Gradually increase brightness
        pwm_pin.write(True)  # Convert to 0.0 - 1.0 range
        time.sleep(0.1)  # Wait for 100 milliseconds

    for value in range(255, -1, -5):  # Gradually decrease brightness
        pwm_pin.write(False)  # Convert to 0.0 - 1.0 range
        time.sleep(0.1)  # Wait for 100 milliseconds

