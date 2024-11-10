from machine import Pin, ADC, PWM
import time

potentiometer = ADC(Pin(26))

buzzer = PWM(Pin(15))
buzzer.freq(1000) 
buzzer.duty_u16(0)

try:
    while True:
        pot_value = potentiometer.read_u16()
        frequency = int(500 + (pot_value / 65535) * 1500)
        
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)

        print("Frequency:", frequency)

        time.sleep(0.1)

except KeyboardInterrupt:
    buzzer.duty_u16(0)
    print("Program stopped by user")
