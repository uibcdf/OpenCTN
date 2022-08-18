import numpy as np

def get_regular_grid_discretization(continuous_chain, ranges=None, deltas=None, n_bins=None):

    n_frames = continuous.shape[0]
    n_dims = continuous.shape[1]

    discrete_chain = np.empty(n_frames, dtype=int)
    microstates = {}

    counter =

    for i in range(n_frames):
        for j in range(n):
            if valores[i][1] >= a+j*h and valores[i][1] < a+(j+1)*h:
                traj_dis[j][1] = j
            if valores[i][2] >= a+j*h and valores[i][2] < a+(j+1)*h:
                traj_dis[j][2] = j
            if valores[i][3] >= a+j*h and valores[i][3] < a+(j+1)*h:
                traj_dis[j][3] = j
        print(str(traj_dis[i][1]) + " " + str(traj_dis[i][2]) + " " + str(traj_dis[i][3]))


    return discrete_chain, microstates
