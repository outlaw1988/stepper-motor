import random
from enum import Enum
from pynput import keyboard

from static import Static


class GPIO:

    pins = {}
    state = 0
    key_listener = None
    current_key = None

    @staticmethod
    def start():
        GPIO.state = 1
        GPIO.key_listener = keyboard.Listener(on_press=GPIO.on_press)
        GPIO.key_listener.start()

    @staticmethod
    def setup(pin, type_in):
        GPIO.pins[pin] = [type_in, 0]

    @staticmethod
    def input(pin):
        if GPIO.current_key == "l" and pin == Static.ROTATION_LEFT_PIN:
            state = 1
        elif GPIO.current_key == "r" and pin == Static.ROTATION_RIGHT_PIN:
            state = 1
        elif GPIO.current_key == "s" and pin == Static.ROTATION_STOP_PIN:
            state = 1
        else:
            state = 0
        print("[INPUT] Pin: %d, state: %d" % (pin, state))
        return state

    @staticmethod
    def output(pin, state):
        print("[OUTPUT] Pin: %d, state: %d" % (pin, state))

    @staticmethod
    def cleanup():
        GPIO.state = 0
        GPIO.pins = {}

    @staticmethod
    def on_press(key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except Exception:
            k = key.name  # other keys

        GPIO.current_key = k
        # if k in ['l', 'r', 's']:  # keys of interest
        #     # self.keys.append(k)  # store it in global-like variable
        #     print('Key pressed: ' + k)
        #     if
        #     # return False  # stop listener; remove this if want more keys


class Type(Enum):
    IN = 0
    OUT = 1
