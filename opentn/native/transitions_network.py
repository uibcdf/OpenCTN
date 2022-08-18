from networkx import Graph

class TransitionsNetwork(Graph):

    def __init__(self, time_step=None, temperature=None):

        self.temperature = None
        self.time_step = None
        self.symmetrized = False

        super().__init__()

