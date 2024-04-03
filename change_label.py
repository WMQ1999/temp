import numpy as np

path = './SEGEMENTED.txt'
mat = np.loadtxt(path)
mat[..., -1] = 5.

np.savetxt(path, fmt='%.3f')