import time
import XInput


def turn_on_vibration_indefinitely(controller):
    """
    Turns on the vibration of the Xbox One controller indefinitely.
    
    :param controller: Controller index (0, 1, 2, or 3).
    """
    while True:
        XInput.set_vibration(controller, 65535, 65535)
        time.sleep(1)  # Sleep to prevent CPU overuse

if __name__ == "__main__":
    controller_index = 0  # Index of the controller you want to vibrate
    turn_on_vibration_indefinitely(controller_index)
