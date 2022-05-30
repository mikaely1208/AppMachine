# !/usr/bin/env python
# from turtlesim_enacter import TurtleSimEnacter # requires ROS
from turtlepy_enacter import TurtlePyEnacter
import random
from Agent2 import Agent2
from Agent3 import Agent3
from Agent5 import Agent5
from OsoyooCarEnacter import OsoyooCarEnacter
ROBOT_IP = "192.168.4.1"


class Agent:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = 0
        self.anticipated_outcome = None
        self.counter = 0
        self.previous_outcome = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
                print("Action: " + str(self._action) +
                      ", Anticipation: " + str(self.anticipated_outcome) +
                      ", Outcome: " + str(outcome) +
                      ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                      ", valence: " + str(self.valence_table[self._action][outcome]) +
                      "; counter: " + str(self.counter) + ")")

        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        # if outcome == self.previous_outcome:
        #     self.counter += 1
        # if self.counter == 4:
        #     if self._action == 0:
        #         self._action = 1
        #     else:
        #         self._action = 0
        #     self.counter = 0
        # self.previous_outcome = outcome





        #     self.previous_outcome = outcome
        # # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = 0
        return self._action


class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """
    def outcome(self, action):
        # return int(input("entre 0 1 ou 2"))
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """

    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


class Environment3:
    """ Environment 3 yields outcome 1 only when the agent alternates actions 0 and 1 """

    def __init__(self):
        """ Initializing Environment3 """
        self.previous_action = 0

    def outcome(self, action):
        _outcome = 1
        if action == self.previous_action:
            _outcome = 0
        self.previous_action = action
        return _outcome



class Environment4:
    def outcome(self, action):
        return random.randint(0, 1)


# TODO Define the hedonist valance of interactions (action, outcome)
valence_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
# a = Agent2(hedonist_table)
a = Agent3(valence_table)
# TODO Choose an environment
e = Environment1()
# e = Environment2()
# e = Environment3()
# e = Environment4()
# e = TurtleSimEnacter()
# e = TurtlePyEnacter()
# e = OsoyooCarEnacter(ROBOT_IP)

if __name__ == '__main__':
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(10):
        action = a.action(outcome)
        outcome = e.outcome(action)