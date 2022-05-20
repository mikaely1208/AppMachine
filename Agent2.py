#!/usr/bin/env python
# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# from turtlesim_enacter import TurtleSimEnacter # requires ROS
from turtlepy_enacter import TurtlePyEnacter
# from Agent5 import Agent5
# from OsoyooCarEnacter import OsoyooCarEnacter
import random


class Agent2:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.compteur = 0
        self.previous_outcome = None
        self.outcome_for_action0 = outcome
        self.outcome_for_action1 = outcome

    def action(self, outcome):
        """ tracing the previous cycle """
      #  if self.previous_outcome == outcome:
       #     self.compteur+=1
        #else:
         #   self.compteur = 0

        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) +
                  ", compteur: " + str(self.compteur) + ")")
        # self.compteur

        """ Computing the next action to enact """

        # TODO: Implement the agent's decision mechanism
        if outcome == 0 and self._action == 0:
            self.outcome_for_action0 = outcome

        if outcome == 1 and self._action == 1:
            self.outcome_for_action1 = outcome

        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = 0
        self.previous_outcome = outcome
        return self._action



