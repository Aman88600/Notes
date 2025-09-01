import pyautogui
from pynput.mouse import Listener

# This function is triggered when a mouse click occurs
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at position: ({x}, {y})")
    # Stop the listener if you click the right button (optional)
    if button == button.right:
        return False

# Setting up the listener for mouse events
with Listener(on_click=on_click) as listener:
    listener.join()
