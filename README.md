# Term-4-assessment
# IoT Device: Potentiometer-Controlled Buzzer

## Project Overview
This project demonstrates a simple IoT device using a potentiometer and a buzzer. The potentiometer controls the frequency of the buzzer, simulating a basic "volume control" device. 

## Components
- **Pico W Microcontroller**
- **Potentiometer** (Analog Input)
- **Buzzer** (PWM Output)
- **Breadboard and Jumper Wires**

## Connections
1. **Potentiometer**: Connect the middle pin to GP26 (ADC0) on the Pico W.
2. **Buzzer**: Connect the positive pin to GP15, and the negative pin to GND.

## Code Explanation
- The potentiometer reads an analog value (0 - 65535) using ADC.
- This value is mapped to a frequency range (500 - 2000 Hz).
- The buzzer tone changes based on the potentiometer position.

## How to Use
1. Rotate the potentiometer to adjust the buzzer's frequency.
2. Observe how the tone changes in response to the potentiometer's position.

## References
- [MicroPython Documentation](https://docs.micropython.org/)
