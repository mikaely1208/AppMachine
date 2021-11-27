# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# Requires:
#   - A robot Osoyoo Car https://osoyoo.com/2019/11/08/omni-direction-mecanum-wheel-robotic-kit-v1/
#   - Project https://github.com/OlivierGeorgeon/osoyoo
#       (First tested with commit c208810 November 27th 2021)
#   - Python libraries pyglet and keyboard
from EgoMemoryWindow import EgoMemoryWindow
import pyglet


class OsoyooCarEnacter:
    def __init__(self):
        """ Instantiating the robot's egocentric spatial memory window """
        self.osoyoo_car_window = EgoMemoryWindow(600)
        self.osoyoo_car_window.zoom_level = 2

        self.osoyoo_car_window.dispatch_events()
        self.osoyoo_car_window.on_draw()
        self.osoyoo_car_window.flip()

    def outcome(self, action):
        """ Enacting an action and returning the outcome """
        outcome = 0
        if action == 0:
            outcome = self.osoyoo_car_window.on_text('8')  # Move forward
        if action == 1:
            outcome = self.osoyoo_car_window.on_text('1')  # Turn left
        if action == 2:
            outcome = self.osoyoo_car_window.on_text('3')  # Turn right

        # Inspired by https://stackoverflow.com/questions/61217265/
        pyglet.clock.tick()
        self.osoyoo_car_window.dispatch_events()
        self.osoyoo_car_window.on_draw()
        self.osoyoo_car_window.flip()

        return int(outcome)


if __name__ == "__main__":
    """ Run in interactive mode """
    e = OsoyooCarEnacter()
    pyglet.app.run()
