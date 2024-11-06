from machine import Pin, ADC, PWM
import time

# Setup the potentiometer on GP26
potentiometer = ADC(Pin(26))  # GP26 corresponds to ADC0 on the Pico W

# Setup the buzzer on GP15 with PWM
buzzer = PWM(Pin(15))  # Use PWM to control the frequency of the buzzer
buzzer.freq(1000)  # Set an initial frequency
buzzer.duty_u16(0)  # Start with the buzzer off

try:
    while True:
        # Read potentiometer value (range is 0 - 65535)
        pot_value = potentiometer.read_u16()
        
        # Map the potentiometer value to a frequency range for the buzzer
        # For instance, map it between 500 Hz to 2000 Hz
        frequency = int(500 + (pot_value / 65535) * 1500)
        
        # Set the buzzer frequency and turn it on
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)  # 50% duty cycle (range is 0 - 65535)

        # Print the frequency for debugging
        print("Frequency:", frequency)
        
        # Short delay to make the change smooth
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up and turn off the buzzer on exit
    buzzer.duty_u16(0)
    print("Program stopped by user")
