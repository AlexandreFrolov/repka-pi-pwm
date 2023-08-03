import RepkaPi.GPIO as GPIO
from time import sleep
import sys

if __name__ == "__main__":

    PWM_chip = 0
    PWM_pin = 0
    frequency_Hz = 1000
    Duty_Cycle_Percent = 8
    led = GPIO.PWM_A(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)

    try:
        while True:
            # Меняем яркость светодиода от минимальной до максимальной
            for duty_cycle in range(0, 101, 5):
                led.start_pwm()  
                led.duty_cycle(duty_cycle)
                sleep(0.1)
                led.stop_pwm()

            for duty_cycle in range(100, -1, -5):
                led.start_pwm()  
                led.duty_cycle(duty_cycle)
                sleep(0.1)
                led.stop_pwm()

    except KeyboardInterrupt:
        # Выход из программы при нажатии Ctrl+C
        pass

    led.pwm_close()
    del led