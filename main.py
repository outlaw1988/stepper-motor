from time import sleep

from gpio import GPIO, Type
from rpi_motor_lib import RpiMotorLib
from threading import Thread

from static import Static


def main():
    initialize_gpio()
    motor = RpiMotorLib(Static.DIRECTION, Static.STEP, Static.GPIO_PINS)

    thread_manage_rotation = Thread(target=manage_rotation,
                                    args=(motor, Static.ROTATION_LEFT_PIN, Static.ROTATION_RIGHT_PIN))
    thread_manage_rotation.start()
    thread_stop_rotation = Thread(target=stop_rotation_listener, args=(Static.ROTATION_STOP_PIN, ))
    thread_stop_rotation.start()
    thread_manage_rotation.join()
    thread_stop_rotation.join()


def initialize_gpio():
    GPIO.start()
    GPIO.setup(Static.ROTATION_LEFT_PIN, Type.IN)
    GPIO.setup(Static.ROTATION_RIGHT_PIN, Type.IN)
    GPIO.setup(Static.ROTATION_STOP_PIN, Type.IN)
    GPIO.setup(Static.OUTPUT_PIN, Type.OUT)


def manage_rotation(motor, rotation_left_pin, rotation_right_pin):
    while True:
        if GPIO.input(rotation_left_pin) == 1:
            GPIO.output(4, 1)
            motor.motor_move("left")
            initialize_gpio()
        elif GPIO.input(rotation_right_pin) == 1:
            GPIO.output(4, 1)
            motor.motor_move("right")
            initialize_gpio()
        else:
            GPIO.output(4, 0)
            sleep(5)


def stop_rotation_listener(rotation_stop_pin):
    while True:
        sleep(1)
        if GPIO.input(rotation_stop_pin) == 1:
            GPIO.cleanup()


if __name__ == '__main__':
    main()
