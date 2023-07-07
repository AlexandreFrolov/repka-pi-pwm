import RepkaPi.GPIO as GPIO
from time import sleep
import sys

def setServoAngle(servo, frequency_Hz, angle):
    servo.start_pwm()  
    dutyCycle = angle / 18. + 3.
    
    print("Угол поворота: " + str(angle) + "\xb0")
    print("Коэффициент заполнения Duty: " + str(dutyCycle) + "%")

    period_duration = 1 / frequency_Hz * 1000
    print("Длительность периода: ", period_duration, "мс, частота " + str(frequency_Hz) + " Гц")
    
    pulse_duration = (period_duration / 100) * dutyCycle
    print("Длительность импульса ШИМ :", round(pulse_duration, 1), "мс")    
    
    servo.duty_cycle(dutyCycle)
    sleep(0.3)
    servo.stop_pwm()

if __name__ == "__main__":

    PWM_chip = 0
    PWM_pin = 0
    frequency_Hz = 50
    Duty_Cycle_Percent = 8
    servo = GPIO.PWM_A(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)

    setServoAngle(servo, frequency_Hz, int(sys.argv[1]))
    servo.pwm_close()
    del servo