# A sample executable to verify the feasibility of mouse click or drag and keyboard entering simulation.

from pymouse import *
from pykeyboard import *
import time


mouse = PyMouse()
keyboard = PyKeyboard()

time.sleep(4)

# mouse click
mouse.click(800, 600)

# mouse drag
# use PyAutoGUI for dragging slowly
mouse.press(720, 640)
mouse.release(880, 720)

# keyboard tap
#keyboard.type_string('12345')
keyboard.tap_key(keyboard.left_key)

# keyboard long press
keyboard.press_key(keyboard.up_key)
time.sleep(2)
keyboard.release_key(keyboard.up_key)

