import RepkaPi.GPIO as GPIO
from time import sleep
import sys

def setServoAngle(servo, angle):
    servo.start_pwm()  
    dutyCycle = angle / 18. + 3.
    print(dutyCycle)
    
    servo.duty_cycle(dutyCycle)
    sleep(0.3)
    servo.stop_pwm()

if __name__ == "__main__":

    PWM_chip = 0
    PWM_pin = 0
    frequency_Hz = 50
    Duty_Cycle_Percent = 8
    servo = GPIO.PWM_A(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)

    setServoAngle(servo, int(sys.argv[1]))
    servo.pwm_close()
    del servo