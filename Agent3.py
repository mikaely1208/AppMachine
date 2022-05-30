# !/usr/bin/env python
import random


class Agent3:

    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.previous_action = 0
        self.anticipated_outcome = None
        self.counter = 0
        self.hedonist_table = [[-1, 1], [-1, 1]]

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
                print("Action: " + str(self._action) +
                      ", Anticipation: " + str(self.anticipated_outcome) +
                      ", Outcome: " + str(outcome) +
                      ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                      ", valence: " + str(self.hedonist_table[self._action][outcome]) +
                      "; counter: " + str(self.counter) + ")")

        if self.hedonist_table[self._action][outcome] == 1:
            return self._action
        else:
            return 0