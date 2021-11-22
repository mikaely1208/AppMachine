# This resource is useful for Agent4

class Interaction:
    interaction_list = []

    def __init__(self, action, outcome, valence):
        self.action = action
        self.outcome = outcome
        self.valence = valence

    def __str__(self):
        return str(self.action) + str(self.outcome) + "(" + str(self.valence) + ")"

    def __hash__(self):
        return self.action * 10 + self.outcome

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.action == other.action) and (self.outcome == other.outcome)
        else:
            return False

    @classmethod
    def create_or_retrieve(cls, action, outcome, valence=0):
        interaction = Interaction(action, outcome, valence)

        if interaction in cls.interaction_list:
            i = cls.interaction_list.index(interaction)
            print("Retrieving ", end="")
            print(cls.interaction_list[i])
            return cls.interaction_list[i]
        else:
            print("Creating ", end="")
            print(interaction)
            cls.interaction_list.append(interaction)
            return interaction


if __name__ == '__main__':
    interaction00 = Interaction.create_or_retrieve(0, 0)
    interaction01 = Interaction.create_or_retrieve(0, 1)
    interaction10 = Interaction.create_or_retrieve(1, 0)
    interaction11 = Interaction.create_or_retrieve(1, 1)
    interaction00 = Interaction.create_or_retrieve(0, 0)
