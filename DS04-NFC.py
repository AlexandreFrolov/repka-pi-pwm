#import RPi.GPIO as GPIO
import RepkaPi.GPIO as GPIO
import time
import warnings

if __name__ == '__main__':
    try:
        PWM_chip = 0
        PWM_pin = 0
        frequency_Hz = 50
        Duty_Cycle_Percent = 0
        servo = GPIO.PWM_A(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)    

        while True:
            pulse_width = float(input("Введите длительность импульса (1-2): "))
            pulse_width = pulse_width / 1000;
            duty = pulse_width / (1 / frequency_Hz) * 100
            print(pulse_width)
            print(duty)
            
            servo.start_pwm()
            servo.duty_cycle(duty)
            time.sleep(10)
            servo.stop_pwm()
    except KeyboardInterrupt:
        servo.pwm_close()
        del servo
        GPIO.cleanup()
