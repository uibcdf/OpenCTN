from networkx import Graph

class KineticTransitionsNetwork(Graph):

    def __init__(self, chain=None, time_step=None, temperature=None):

        self.temperature = None
        self.time_step = None
        self.symmetrized = False

        super().__init__()

    def add_transitions_from_discrete_chain(self, discrete_chain, states=None)

        pass

    def get_stochastic_matrix(self, states=None)

        pass

