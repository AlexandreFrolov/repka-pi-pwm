import RepkaPi.GPIO as GPIO
import time
import threading

GPIO.setboard(GPIO.REPKAPI3)
GPIO.setmode(GPIO.SUNXI)

servo_pin = "PA8"
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setwarnings(False)

def set_servo_angle(angle, frequency_Hz):
    dutyCycle = angle / 18. + 3.
    period_duration = 1 / frequency_Hz * 1000
    pulse_duration = ((period_duration / 100) * dutyCycle)
    wait_after_pulse = period_duration - round(pulse_duration, 1)
    
    GPIO.output(servo_pin, GPIO.HIGH)
    threading.Timer(pulse_duration / 1000.0, lambda: GPIO.output(servo_pin, GPIO.LOW)).start()
    threading.Timer(wait_after_pulse / 1000.0, lambda: set_servo_angle(angle, frequency_Hz)).start()

try:
    threading.Timer(2, lambda: set_servo_angle(0, 50)).start()

except KeyboardInterrupt:
    GPIO.cleanup()