# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# It requires:
#   A robot Osoyoo Car https://osoyoo.com/2019/11/08/omni-direction-mecanum-wheel-robotic-kit-v1/
#   Project https://github.com/OlivierGeorgeon/osoyoo
#   Python libraries pyglet and keyboard
from EgoMemoryWindow import EgoMemoryWindow
import pyglet

class OsoyooCarEnacter:
    def __init__(self):
        self.em_window = EgoMemoryWindow()
        pyglet.app.run()

    def outcome(self, action):
        """ Enacting an action and returning the outcome """
        outcome = 0
        if action == 0:
            outcome = self.em_window.outcome('8')
        if action == 1:
            outcome = self.em_window.outcome('1')
        if action == 2:
            outcome = self.em_window.outcome('3')
        return int(outcome)


if __name__ == "__main__":
    e = OsoyooCarEnacter()
