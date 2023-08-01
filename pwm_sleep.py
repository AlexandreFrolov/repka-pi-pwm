import RepkaPi.GPIO as GPIO
import time

GPIO.setboard(GPIO.REPKAPI3)
GPIO.setmode(GPIO.SUNXI)

servo_pin = "PA8"
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setwarnings(False)

def set_servo_angle(angle, frequency_Hz):
    dutyCycle = angle / 18. + 3.
    period_duration = 1 / frequency_Hz * 1000 # период в мс
    pulse_duration = ((period_duration / 100) * dutyCycle) # длительность импульса в мс
    wait_after_pulse = period_duration - round(pulse_duration, 1) # время ожидания для завершение цикла в мс
    
    GPIO.output(servo_pin, GPIO.HIGH)  # Устанавливаем пин в HIGH
    time.sleep((pulse_duration /  1000.0)) # перевод задержки в секунды
    GPIO.output(servo_pin, GPIO.LOW)  # Устанавливаем пин в LOW
    time.sleep(wait_after_pulse / 1000.0)
    
try:
    while True:
        set_servo_angle(0, 50)

except KeyboardInterrupt:
    GPIO.cleanup()

