import time
import pyperclip
from pynput.keyboard import Key, Controller


def getvarnpaste(variable):
    pyperclip.copy(variable)

    keyboard = Controller()
    time.sleep(1)
    keyboard.press(Key.ctrl.value)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl.value)
    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
