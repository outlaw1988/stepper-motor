from time import sleep
from gpio import GPIO


class RpiMotorLib:

    def __init__(self, direction, step, pins):
        self.direction = direction
        self.step = step
        self.pins = pins

    def motor_move(self, rotation_direction):
        for _ in range(30):
            if GPIO.state == 1:
                sleep(5)
                print("Direction: %s, step: %d" % (rotation_direction, self.step))
                print("Motor rotation in progress...")
            else:
                print("Motor rotation stopped")
                break
