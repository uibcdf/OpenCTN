import numpy as np

def get_regular_grid_discretization(continuous_chain, ranges=None, deltas=None, n_bins=None):
    """Discretization of a continuous-space multidimensional chain with a regular grid

    Given a multidimensional continous-space chain and a regular grid, the corresponding
    discrete-space chain is obtained.

    Parameters
    ----------
    continous_chain : ndarray, (list or tuple) of (lists or tuples)
        The multidimensional continuous-space chain to be discretized as a Numpy ndarray with shape
        [n_steps, n_dims], or similar object made by lists or tuples.

    Return
    ------
    discrete_chain : ndarray
        Resultant chain with the sequence of new discrete states indices as a Numpy
        ndarray of shape [n_steps].

    states: dict
        Dictionary with the states indices as keys and their lists of bin limits as values. The bin limits are
        always closed in the inferior limit and open in the superior limit: x belongs to [lim_inf,
        lim_sup] if lim_inf <= x < lim_sup.

    Examples
    --------
    >>> import openktn as oktn
    >>> cont_chain = [[ 0.1,  2.0,  0.6]
    >>>               [ 0.3,  2.1,  1.1]
    >>>               [ 0.9,  1.8,  1.6]
    >>>               [ 1.3,  1.4,  1.7]
    >>>               [ 0.8,  1.1,  1.2]
    >>>               [ 1.2,  0.3,  0.8]]
    >>> disc_chain, states = oktn(cont_chain, ranges=[[0.0, 1.5], [0.0, 2.5], [0.0, 2.0]], n_bins=[3, 5, 4])
    >>> disc_chain
    [0,1,2,3,2,4]
    >>> states
    {0:[[0.0, 0.5], [2.0, 2.5], [0.5, 1.0]], 1:[[0.0, 0.5], [2.0, 2.5], [1.0, 1.5]],
    2:[[0.5, 1.0], [1.5, 2.0], [1.5, 2.0]], 3:[[1.0, 1.5], [1.0, 1.5], [1.0, 1.5]],
    4:[[1.0, 1.5], [0.0, 0.5], [0.5, 1.0]]}
    """

    n_steps, n_dims = continuous_chain.shape[:]

    discrete_chain = np.empty(n_steps, dtype=int)
    states = {}

    # implement here


    return discrete_chain, microstates
