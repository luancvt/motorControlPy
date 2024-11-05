import time
import sys
sys.path.append('/home/username/.local/lib/python3.10/site-packages')

from pyfirmata import Arduino, util

# Set up the connection to the Arduino board
board = Arduino('/dev/ttyACM0')  # Adjust for your operating system

# Define the digital pin 3 as output
led_pin = board.get_pin('d:6:o')

# Define the digital pin 3 as pwm
pwm_pin = board.get_pin('d:3:p') 

board.digital[3].mode = 3  # 3 is the PWM mode in pyfirmata
print("P3: ", board.digital[3].mode)
print("P6: ", board.digital[6].mode)

# Set a PWM duty cycle
# A value between 0 and 1, where 1 = 100% duty cycle (fully on), 0 = 0% (off)
duty_cycle = 0.5  # 50% duty cycle

board.digital[3].write(0)
time.sleep(5)

# Write the duty cycle to the PWM pin
board.digital[3].write(duty_cycle)

# Keep the PWM signal on for 5 seconds
time.sleep(5)

# Turn off the PWM signal
board.digital[3].write(0)

# while True:
#     # # Simple blinking code
#     # led_pin.write(True)  
#     # time.sleep(0.1)
#     # led_pin.write(False) 
#     # time.sleep(0.1)

#     pwm_pin.write(0)

#     # for i in range(0, 256):  # i ranges from 0 to 100
#         # # dt = i/255
#         # # print("DT: ", dt)
#         # pwm_pin.write(0.5)
#         # print("Iteration: ", i)
#         # time.sleep(0.5)  # small delay
#         # pwm_pin.write(0.9)
#         # time.sleep(0.5)