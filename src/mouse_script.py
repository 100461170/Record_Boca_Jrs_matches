from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Give yourself a few seconds to switch to the desired window
time.sleep(5)

# click play
# machine dependent
mouse.position = (957, 330)
mouse.click(Button.left)
time.sleep(0.5)  # Optional delay

# Click full screen
mouse.position = (1314, 523)
mouse.click(Button.left)

# manual algorithm to get the positions needed
""" while True:
    # Get the current mouse position
    position = mouse.position

    print(f"The current mouse position is: {position}") """
