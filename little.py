import RPi.GPIO as GPIO
import time
output_pin = 18  
def main():

    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    now=time.time()
    try:
        while True:
            if(time.time()-now <1):
                GPIO.output(output_pin,GPIO.HIGH)
                time.sleep(1/1000)
                GPIO.output(output_pin,GPIO.LOW)
                time.sleep(19/1000)
            elif(time.time()-now <2):
                GPIO.output(output_pin,GPIO.HIGH)
                time.sleep(2/1000)
                GPIO.output(output_pin,GPIO.LOW)
                time.sleep(18/1000)
            else:
                now=time.time()
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()