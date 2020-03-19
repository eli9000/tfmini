import RPi.GPIO as GPIO
import time

buzz = 11
green_led = 40
red_led = 38
blue_led = 36


def setup():
    GPIO.setmode(GPIO.BOARD)    # Uses physical numbers for pins
    GPIO.setup(buzz, GPIO.OUT)
    GPIO.output(buzz, GPIO.LOW)

    GPIO.setup(green_led, GPIO.OUT)
    GPIO.setup(red_led, GPIO.OUT)
    GPIO.setup(blue_led, GPIO.OUT)


def loop():
    for i in range(100):
        if i % 3 == 0:
            print("GREEN: {} = 0 mod 3".format(i))
            GPIO.output(green_led, 1)
            time.sleep(0.5)
            GPIO.output(green_led, 0)
        elif i % 7 == 0:
            print("BLUE: {} = 0 mod 7".format(i))
            GPIO.output(blue_led, 1)
            time.sleep(0.5)
            GPIO.output(blue_led, 0)
        elif i % 11 == 0:
            print("RED: {} = 0 mod 11".format(i))
            GPIO.output(red_led, 1)
            GPIO.output(buzz, 1)
            time.sleep(0.5)
            GPIO.output(buzz, 0)
            GPIO.output(red_led, 0)
        GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Goodbye!")
